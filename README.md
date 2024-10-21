# WhatsApp Chat Converter

## Description
A Python tool to convert WhatsApp chat logs into HTML and PDF formats.  
This tool allows you to display your WhatsApp chats in appealing HTML documents and optionally convert them to PDF files.

## Example
This is the exported _chat.txt file:  
![image](https://github.com/aquamarine-guy/WhatsApp-Chat-Converter/assets/174265589/83bc713b-13a3-4498-9330-94239b4f6fce)

Which will transform into this more visualized HTML or optionally also a PDF file that almost looks exactly like a real WhatsApp chat:  
![image](https://github.com/aquamarine-guy/WhatsApp-Chat-Converter/assets/174265589/710430b5-4a11-491e-af44-7a60ffd62937)

## Features
- Convert WhatsApp chat logs to HTML
- Optional PDF export
- Embed CSS in HTML (if desired)
- Support for multiple ZIP files in one go
- Each media item is opened in your browser with one hyperlink click (JPG, PNG, PDF, audio files, etc.)

## Requirements
- Python 3.10
- [wkhtmltopdf](https://github.com/JazzCore/python-pdfkit/wiki/Installing-wkhtmltopdf) (Install and put the `wkhtmltopdf` executable in the project root or add it to your PATH environment variable)

### Python Packages
Install the following Python packages using `pip`:
  ```bash
  pip install pdfkit
```
 ```bash
pip install tk
```
### Standard Libraries
The following Python standard libraries are used and do not need to be installed separately as they are included with Python:
- zipfile
- io
- os
- shutil
- datetime

## Usage
1. Export your WhatsApp chat in the WhatsApp app on your phone. Full instructions on how to do this can be found here: [WhatsApp FAQ](https://faq.whatsapp.com/1180414079177245/?locale=en_EN&cms_platform=android)
   
2. Run the Python script:

3. Use the graphical user interface to:
- Select the path to your WhatsApp ZIP files (multiple ZIPs at once are possible).
- Set the output directory.
- Enable or disable the option to embed CSS in HTML.
- Enable or disable the option to create PDF files (only available if you enable the option to embed the CSS into the HTML file).
- Click "Start" to begin the conversion process.<br>

![image](https://github.com/aquamarine-guy/WhatsApp-Chat-Converter/assets/174265589/f8c36837-68ff-4e1c-bd26-57fc5e01569d)

## Future Improvements
Please let me know if I should add anything or if you have ideas for future projects you want to see. <br>
I want to improve my coding and need ideas/challenges to tackle. Your feedback and suggestions are highly appreciated!

## German-Version of the Script
*coming soon*
(optionally just change the word "Attachment" in line 60 of the script to "Anhang", than everything should work again even in german)
