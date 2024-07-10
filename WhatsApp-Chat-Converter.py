import zipfile
import os
from datetime import datetime
import re
import tkinter as tk
from tkinter import filedialog, messagebox
import pdfkit

def parse_chat_line(line):
    try:
        parts = line.split("] ")
        if len(parts) < 2:
            return None
        timestamp = parts[0].strip("[]\u200e")
        sender_message = parts[1].split(": ", 1)
        if len(sender_message) < 2:
            return None
        sender = sender_message[0]
        message = sender_message[1]
        return timestamp, sender, message
    except Exception as e:
        print(f"Error processing line: {line} - {e}")
        return None

def create_html(chat_lines, self_name, css_inline, chat_name):
    css_content = """
    body { font-family: Arial, sans-serif; background-color: #e5ddd5; }
    .chat { margin: auto; max-width: 600px; }
    .message { padding: 10px; margin: 5px; border-radius: 10px; }
    .self { background-color: #dcf8c6; text-align: right; }
    .other { background-color: #fff; text-align: left; }
    .timestamp { display: block; font-size: 0.8em; color: gray; }
    """

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">"""
    
    if css_inline:
        html += f"<style>{css_content}</style>"
    else:
        html += '<link rel="stylesheet" href="styles.css">'

    html += f"""<title>WhatsApp Chat - {chat_name}</title>
</head>
<body>
<div class="chat">"""

    for line in chat_lines:
        if line:
            timestamp, sender, message = line
            try:
                timestamp_str = datetime.strptime(timestamp, "%d.%m.%y, %H:%M:%S").strftime("%d.%m.%Y %H:%M")
            except ValueError:
                timestamp_str = timestamp
            
            message_class = "self" if sender != self_name else "other"
            media_match = re.search(r"<Attachment: (.+?)>", message)
            
            if media_match:
                media_file = media_match.group(1).strip()
                message_content = f'<a href="media/{media_file}" target="_blank">{media_file}</a>'
            else:
                message_content = f'<span class="text">{message}</span>'

            html += f'<div class="message {message_class}"><span class="sender">{sender}:</span> {message_content} <span class="timestamp">{timestamp_str}</span></div>'

    html += """</div>
</body>
</html>"""
    return html, css_content

def process_zip(zip_path, output_dir, css_inline, create_pdf):
    zip_name = os.path.basename(zip_path).replace("WhatsApp Chat - ", "").replace(".zip", "")
    
    chat_dir = os.path.join(output_dir, f"chat_output_{zip_name}")
    media_dir = os.path.join(chat_dir, "media")

    try:
        os.makedirs(media_dir, exist_ok=False)
    except FileExistsError:
        return f"The folder '{chat_dir}' already exists. Please delete or rename it."
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(media_dir)

    chat_file_path = os.path.join(media_dir, "_chat.txt")
    if os.path.exists(chat_file_path):
        with open(chat_file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            other_name = zip_name
            self_name = None
            if lines:
                first_line = parse_chat_line(lines[0])
                if first_line:
                    self_name = first_line[1] if first_line[1] != other_name else other_name

            chat_lines = [parse_chat_line(line) for line in lines if line.strip()]
            chat_lines = [line for line in chat_lines if line]

        html_content, css_content = create_html(chat_lines, self_name, css_inline, zip_name)

        html_file_name = f"chat_{zip_name}.html"
        html_file_path = os.path.join(chat_dir, html_file_name)
        with open(html_file_path, 'w', encoding='utf-8') as html_file:
            html_file.write(html_content)

        if not css_inline:
            with open(os.path.join(chat_dir, "styles.css"), 'w', encoding='utf-8') as css_file:
                css_file.write(css_content)
        
        if create_pdf:
            try:
                options = {
                    'enable-local-file-access': None
                }
                pdf_file_name = f"chat_{zip_name}.pdf"
                pdf_file_path = os.path.join(chat_dir, pdf_file_name)
                pdfkit.from_file(html_file_path, pdf_file_path, options=options)
            except Exception as e:
                return f"Error creating PDF: {e}"
        
        return f"Chat successfully created in folder: {chat_dir} (HTML: {html_file_name}, PDF: {pdf_file_name if create_pdf else 'not created'})"
    else:
        return "The file '_chat.txt' was not found."

def main():
    root = tk.Tk()
    root.title("WhatsApp Chat Converter")

    tk.Label(root, text="Path to ZIP file:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    zip_path_var = tk.StringVar()
    tk.Entry(root, textvariable=zip_path_var, width=50).grid(row=0, column=1, padx=10, pady=5)
    tk.Button(root, text="Browse", command=lambda: zip_path_var.set(",".join(filedialog.askopenfilenames(filetypes=[("ZIP files", "*.zip")])))).grid(row=0, column=2, padx=10, pady=5)

    tk.Label(root, text="Output folder:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    output_dir_var = tk.StringVar()
    tk.Entry(root, textvariable=output_dir_var, width=50).grid(row=1, column=1, padx=10, pady=5)
    tk.Button(root, text="Browse", command=lambda: output_dir_var.set(filedialog.askdirectory())).grid(row=1, column=2, padx=10, pady=5)

    css_inline_var = tk.BooleanVar()
    tk.Checkbutton(root, text="Embed CSS in HTML", variable=css_inline_var).grid(row=2, column=1, padx=10, pady=5, sticky="w")

    create_pdf_var = tk.BooleanVar()
    pdf_checkbox = tk.Checkbutton(root, text="Create PDF", variable=create_pdf_var)
    pdf_checkbox.grid(row=3, column=1, padx=10, pady=5, sticky="w")

    def update_pdf_checkbox():
        if not css_inline_var.get():
            pdf_checkbox.config(state=tk.DISABLED)
            create_pdf_var.set(False)
        else:
            pdf_checkbox.config(state=tk.NORMAL)
    
    css_inline_var.trace_add('write', lambda *args: update_pdf_checkbox())
    update_pdf_checkbox()  # Initial call to set the correct state

    def start_conversion():
        zip_paths = zip_path_var.get().split(',')
        output_dir = output_dir_var.get()
        css_inline = css_inline_var.get()
        create_pdf = create_pdf_var.get()
        
        if not zip_paths or not output_dir:
            messagebox.showerror("Error", "Please provide path to ZIP file and output folder.")
            return
        
        results = []
        for zip_path in zip_paths:
            result = process_zip(zip_path.strip(), output_dir, css_inline, create_pdf)
            if result:
                results.append(result)
        
        messagebox.showinfo("Result", "\n".join(results))

    tk.Button(root, text="Start", command=start_conversion).grid(row=4, column=1, padx=10, pady=20)
    
    root.mainloop()

if __name__ == "__main__":
    main()
