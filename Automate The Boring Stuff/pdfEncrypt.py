# This script encrypts all the pdf-s in the given user directory
import tkinter.filedialog, importlib, os, sys, logging
logging.basicConfig(filename = 'pdfEncrypt.log', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(lineno)s - %(message)s',
                    datefmt = '%d/%m/%Y %I:%H:%S %p', filemode = 'w')

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
    logging.debug(f'{sys.argv = }')
    if len(sys.argv) < 2: 
        sys.exit('Usage: python pdfEncrypt.py <password>')
 
    directory = os.path.normpath(tkinter.filedialog.askdirectory());            logging.info(f'{directory = }')
    if not directory:
        sys.exit('No directory chosen')
    
    for dir, subdir, filenames in os.walk(directory):
        for filename in filenames:
            # TODO: Encrypt all the pdf's using pypdf2 module
            if os.path.splitext(filename)[1] == '.pdf':
                print('Found file %s' % (filename));                            logging.debug(f'{dir = }\n{subdir = }\n{filename = }')
                with open(os.path.join(dir, filename), 'rb') as pdffile:
                    pdfInput = pypdf2.PdfFileReader(pdffile)
                    if pdfInput.isEncrypted:
                        print('File %s is already encrypted')
                        os.rename(dir + os.sep + filename, os.path.splitext(filename)[0] + '_encrypted.pdf')
                        continue

                    pdfOutput = pypdf2.PdfFileWriter()
                    for i in range(pdfInput.numPages):
                        pdfOutput.addPage(pdfInput.getPage(i))
                    pdfOutput.encrypt(sys.argv[1])

                    outputFilename = os.path.splitext(filename)[0] + '_encrypted.pdf';  logging.debug(f'{outputFilename = }')
                    with open(outputFilename, 'wb') as outputFile:
                        pdfOutput.write(outputFile)                                    


# TODO: Save the encrypted files with _encrypted.pdf suffix
# TODO: Check if the encryption was successful by checking if encrypted and try to decrypt
# TODO: Delete the original file

if __name__ == '__main__':
    main()
