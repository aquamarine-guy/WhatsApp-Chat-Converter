# WhatsApp Chat Converter

## Description
A Python tool to convert WhatsApp chat logs into HTML and PDF formats.  
This tool allows you to display your WhatsApp chats in appealing HTML documents and optionally convert them to PDF files.

## Example:
This is the exported _chat.txt file:  
![image](https://github.com/aquamarine-guy/WhatsApp-Chat-Converter/assets/174265589/1880e191-99ac-4a44-be71-887ac58a16e4)

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
- Click "Start" to begin the conversion process.

## German-Version of the Script
*cooming soon*
