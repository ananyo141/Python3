#!python3
# This is the counterpart of program pdfParanoiaP1
import tkinter.filedialog, os, sys, logging, shutil
from ModuleImporter import module_importer
# filename = 'pdfParanoiaP2.log'
logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(lineno)s - %(message)s',
                    datefmt = '%d/%m/%Y %I:%H:%S %p', filemode = 'w')
# logging.disable(logging.CRITICAL)

# import third-party modules safely
pypdf2 = module_importer('PyPDF2', 'PyPDF2')
pyip = module_importer('pyinputplus', 'pyinputplus')

def main():
    # TODO: Ask the user for a directory
    directory = tkinter.filedialog.askdirectory()
    if not directory:
        sys.exit('No directory chosen')
    directory = os.path.normpath(directory)

    # TODO: Ask the user for password
    passw = pyip.inputPassword(prompt = 'Enter the password of the PDFs: ')

    # TODO: Find all the encrypted pdf's in the directory
    for dir, subdir, filenames in os.walk(directory):
        for filename in filenames:
            if os.path.splitext(filename)[1] == '.pdf':

        
    # TODO: Create decrypted copy of the file
    # TODO: If password incorrect, warn the user and continue
