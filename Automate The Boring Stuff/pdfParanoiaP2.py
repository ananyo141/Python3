#!python3
# This is the counterpart of program pdfParanoiaP1
import tkinter.filedialog, os, sys, logging, shutil
from ModuleImporter import module_importer
logging.basicConfig(filename='pdfParanoiaP2.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(lineno)s - %(message)s',
                    datefmt = '%d/%m/%Y %I:%H:%S %p', filemode = 'w')
# logging.disable(logging.CRITICAL)

# import third-party modules safely
pypdf2 = module_importer('PyPDF2', 'PyPDF2')
pyip = module_importer('pyinputplus', 'pyinputplus')

def main():
    # Ask the user for a directory
    openDirectory = tkinter.filedialog.askdirectory()
    if not openDirectory:
        sys.exit('No directory chosen')
    openDirectory = os.path.normpath(openDirectory);                                logging.debug(f'{openDirectory = }')

    # Ask the user for password
    passw = pyip.inputPassword(prompt = 'Enter the password of the PDFs: ')

    # Find all the encrypted pdf's in the directory
    saveDir = os.path.join(openDirectory, 'Decrypted Files');                       logging.info(f'{saveDir = }')
    for dir, subdir, filenames in os.walk(openDirectory):
        for filename in filenames:
            if os.path.splitext(filename)[1] == '.pdf':
                os.makedirs(saveDir, exist_ok = True)
                with open(os.path.join(dir, filename), 'rb') as pdfFile:
                    pdfFileReader = pypdf2.PdfFileReader(pdfFile)
                    # skip if not encrypted
                    if not pdfFileReader.isEncrypted:
                        continue
                    # If password incorrect, warn the user and continue
                    print(f"Found encrypted file: {filename}");                     logging.debug(f'{filename = }')
                    if not pdfFileReader.decrypt(passw):
                        print(f"Could not decrypt {filename}: Invalid Password")
                        continue
                    # create a decrypted version
                    pdfFileWriter = pypdf2.PdfFileWriter()
                    for i in range(pdfFileReader.numPages):
                        pdfFileWriter.addPage(pdfFileReader.getPage(i))
                    savefilename = os.path.splitext(os.path.basename(filename))[0] + '_decrypted.pdf';   logging.debug(f'{savefilename = }')
                    with open(os.path.join(saveDir, savefilename), 'wb') as saveFile:
                        pdfFileWriter.write(saveFile)
                    print(f"Decrypted file: {savefilename}")
                        
    if os.path.exists(saveDir):
        print(f'Decrypted files saved at {saveDir}')
        

if __name__ == '__main__':
    main()
