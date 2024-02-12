# GUI QR CODE GENERATOR w/ Python
#### [Video Demo](https://www.youtube.com/watch?v=K8L6KVGG-7o)
#### Description:
A simple <span style="color: #2581f7">GUI qr code generator</span>, implemented using <b>`PyQt6 framework`</b>, <b>`qr library`</b>,<b>`PIL library`</b>.

## INSTALLATION:
1. clone the repo or download the files manually.
2. Install the dependencies <span style="color: #2581f7">(preferably in a virtual environment)</span>.
```bash
pip install -r requirements.txt
```
3. When in the project directory run:
```bash
python ./project.py #on winodws type python .\project.py
```

## Overview
The app features a simple interface, with multiple widgets:
- an input text area that holds the text the user wants to encode in a qr code
- a clear button the clears the text so that the user doesn't have to delete the text manually.
- a filename input field so the user can customize the name of the outputed qr code, this field is required, if left empty a pop-up message box will appear and addresses the issue.
- a drop-down menu with three options to control the size (quality) of the qr code *(high,medium,low)* high being the largest.
- a drop-down menu with four options to control the fill color of the qr code (black, green, red, blue).
- a generate button, when clicked the data in the text area will be encoded to a qr code and saved in the same directory of the <span style="color: #2581f7">project.py</span> file, if the text area is empty a pop-up message box will appear and addresses the issue.
- a quit button, when clicked the application exits.

