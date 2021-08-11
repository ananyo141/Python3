# This script encrypts all the pdf-s in the given user directory
import tkinter.filedialog, importlib, os, sys, logging, shutil
# filename = 'pdfEncrypt.log'
logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(lineno)s - %(message)s',
                    datefmt = '%d/%m/%Y %I:%H:%S %p', filemode = 'w')
logging.disable(logging.CRITICAL)

def module_importer(module_name, package_name):
    '''(str, str) -> ModuleType
    Read the module name as a string and try to import it normally,
    failing which tries to download required package and return the module.
    '''
    try:
        return importlib.import_module(module_name)
    except ModuleNotFoundError:
        print('Resolving dependencies...')
        print(f'Required Module: {package_name}')
        try:
            os.system('pip install ' + package_name)
            return importlib.import_module(module_name)
        except Exception as e:
            sys.exit(str(e))

# import third-party modules safely
pypdf2 = module_importer('PyPDF2', 'PyPDF2')
pyip = module_importer('pyinputplus', 'pyinputplus')

def main():    
    directory = tkinter.filedialog.askdirectory();            
    if not directory:
        sys.exit('No directory chosen')
    # make the directory os specific
    directory = os.path.normpath(directory);                                    logging.info(f'{directory = }')

    passw = pyip.inputPassword(prompt = 'Enter the password you want to encrypt the PDFs with: ')

    saveDir = directory + os.sep + 'Encrypted Files' + os.sep;                 logging.info(f'{saveDir = }')
    for dir, subdir, filenames in os.walk(directory):
        for filename in filenames:
            # Encrypt all the pdf's using pypdf2 module
            if os.path.splitext(filename)[1] == '.pdf':
                os.makedirs(saveDir, exist_ok = True)
                print('Encrypting file %s...' % (filename));                            logging.debug(f'{dir = }\n{filename = }')
                filepath = os.path.join(dir, filename);                         logging.debug(f'{filepath = }')
                with open(filepath, 'rb') as pdffile:
                    pdfInput = pypdf2.PdfFileReader(pdffile)
                    if pdfInput.isEncrypted:
                        print('File %s is already encrypted' % (filename))
                        pdffile.close()
                        shutil.move(filepath, saveDir + os.path.splitext(filename)[0] + '_encrypted.pdf')
                        continue

                    pdfOutput = pypdf2.PdfFileWriter()
                    for i in range(pdfInput.numPages):
                        pdfOutput.addPage(pdfInput.getPage(i))
                    pdfOutput.encrypt(passw)

                    # Save the encrypted files with _encrypted.pdf suffix
                    outputFilename = saveDir + os.path.splitext(filename)[0] + '_encrypted.pdf';  logging.debug(f'{outputFilename = }')
                    with open(outputFilename, 'wb') as outputFile:
                        pdfOutput.write(outputFile)     
                    # Check if the encryption was successful by checking if encrypted and try to decrypt
                    with open(outputFilename, 'rb') as reopenedFile:
                        reopenPDF = pypdf2.PdfFileReader(reopenedFile)
                        if not reopenPDF.isEncrypted:
                            print(f'{outputFilename} encryption unsuccessful')
                            continue
                        try:
                            reopenPDF.decrypt(passw)
                            reopenPDF.getPage(0)
                        except:
                            print(f'{outputFilename} cannot be opened after encryption')
                            continue
                # Delete the original file
                os.unlink(filepath)

    if os.path.exists(saveDir):
        print('Files saved in %s' % (saveDir))                               


if __name__ == '__main__':
    main()
