import sys,os
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtGui as qtg

def generate_qr_code(data, quality, color,filename):
    """This function generates a qr code and saves it to the current working directory
    Args:
        data (str): The data to be encoded in the qr code
        quality (int): The qr code quality
        color (str): The qr code fill color
        filename (str): The filename to save the qr code to
    """
    import qrcode,os
    cur_dir = os.getcwd()

    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=quality,
        border=4,
    )
    
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create an image from the QR code
    img = qr.make_image(fill_color=color, back_color="white")

    # Save the image
    if get_os() == "Windows":
        img.save(cur_dir+'\\'+filename+'.png')
        os.startfile(cur_dir+'\\'+filename+'.png')
    else:
        import subprocess
        img.save(cur_dir+'/'+filename+'.png')
        subprocess.run(['xdg-open', cur_dir+'\\'+filename+'.png'])

def get_os()->str:
    """Get the current operating system"""
    import platform
    sysm = platform.system()
    return sysm
def main():
    app = qtw.QApplication(sys.argv)
    app.setApplicationName("Hamza's Qr Code Gen")
    app_icon = qtg.QIcon(r'graphics/qr-code.png')
    app.setWindowIcon(app_icon)
    font = qtg.QFont("Cascadia Code", 10)  
    app.setFont(font)
    mw = MainWindow()
    app.setStyleSheet("""
        QWidget {
            background-color: #212121;
            color: white;
        }
        QTextEdit{
            background-color: lightgray;
            color: #212121;
            border-radius: 5;
        }
        QPushButton {
            background-color: #0077b6; 
            color: white;
            padding: 7px;
            border-radius: 5px;
        }
        QLineEdit{
            background-color: #f0f0f0;
            border: 1px solid #e0e0e0;
            padding: 5px;
            color: #212121;
            min-width: 6em;
            border-radius: 5;
        }
        QPushButton:hover {
            background-color: #00b4d8; 
        }
        QComboBox {
            background-color: #f0f0f0;
            border: 1px solid #e0e0e0;
            color: #212121;
            padding: 5px;
            min-width: 6em;
            border-radius: 5;
        }
        QComboBox::drop-down {
            subcontrol-origin: padding;
            subcontrol-position: right top;
            width: 10px;
            border-left: 1px solid #e0e0e0;
        }
        QComboBox QAbstractItemView {
            border: 1px solid #e0e0e0;
            selection-background-color: lightblue;
            border-radius: 5;
        }
    """)
    sys.exit(app.exec())

class FilenameValidator(qtg.QValidator):
    """Enforce valid filenames"""
    def validate(self, string, index):
        if not string:
            # An empty string is considered Intermediate
            return (qtg.QValidator.State.Intermediate, string, index)
        try:
            # Check if the string is a valid filename
            if os.path.exists(string) or not os.path.basename(string):
                state = qtg.QValidator.State.Invalid
            else:
                state = qtg.QValidator.State.Acceptable
        except Exception:
            # Handle exceptions that might occur during validation
            state = qtg.QValidator.State.Invalid
        return (state, string, index)

class MainWindow(qtw.QWidget):
    def __init__(self):
        """MainWindow Constructor"""
        super().__init__()
        #Main UI code
        main_layout = qtw.QFormLayout()
        #sizing the window
        self.setLayout(main_layout)
        self.setMaximumWidth(300)
        self.setMaximumHeight(450)
        self.setMinimumHeight(450)
        self.setMinimumWidth(300)

        #text to be encoded
        self.text_to_encode = qtw.QTextEdit(self)
        main_layout.addRow(self.text_to_encode)
        self.clear_button = qtw.QPushButton('Clear',self)
        clear_icon = qtg.QIcon(r'graphics/bin.png')
        self.clear_button.setIcon(clear_icon)
        self.clear_button.clicked.connect(self.clear_text_edit)
        main_layout.addRow(self.clear_button)

        #custom file name
        self.custom_output_name = qtw.QLineEdit(self)
        self.custom_output_name.setValidator(FilenameValidator())
        self.custom_output_name.setClearButtonEnabled(True)
        self.custom_output_name.setMaxLength(20)
        main_layout.addRow('file name',self.custom_output_name)

        #Qr code quality 
        self.qr_quality = qtw.QComboBox(self)
        self.qr_quality.addItem('High',30)
        self.qr_quality.addItem('Medium',20)
        self.qr_quality.addItem('Low',10)
        main_layout.addRow('quality',self.qr_quality)

        #fill colors menu
        self.fill_color = qtw.QComboBox(self)
        self.fill_color.addItem('Black','black')
        self.fill_color.addItem('Green','green')
        self.fill_color.addItem('Red','red')
        self.fill_color.addItem('Blue','blue')
        main_layout.addRow('fill color',self.fill_color)

        #generate button
        self.gen_button = qtw.QPushButton(' Generate Qr Code',self)
        gen_icon = qtg.QIcon(r'graphics/qr-code.png')
        self.gen_button.setIcon(gen_icon)
        self.gen_button.clicked.connect(lambda: generate_qr_code(
            self.text_to_encode.toPlainText(),self.qr_quality.currentData(),
            self.fill_color.currentData(),self.custom_output_name.text()
        ))
        main_layout.addRow(self.gen_button)

        #quit button
        self.quitbutton = qtw.QPushButton('Quit')
        quit_icon = qtg.QIcon(r"graphics/button.png")
        self.quitbutton.setIcon(quit_icon)
        self.quitbutton.clicked.connect(self.close)
        main_layout.addRow(self.quitbutton)
        #END UI code
        self.show()
    def clear_text_edit(self):
        self.text_to_encode.clear()

if __name__ == "__main__":
    main()