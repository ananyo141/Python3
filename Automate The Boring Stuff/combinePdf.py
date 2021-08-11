# This script combines the pdfs into a single pdf and uses various features.
import tkinter.filedialog
import logging
import os
from ModuleImporter import module_importer

# filename='combinepdf.log'
logging.basicConfig(level=logging.DEBUG, filemode='w',
                    format='%(asctime)s - %(levelname)s - %(lineno)d - %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
logging.disable(logging.CRITICAL)

# import the third-party modules safely
pypdf2 = module_importer('PyPDF2')
pyip = module_importer('pyinputplus')

def main():
    logging.debug('Starting program execution')
    # Give the user a gui to enter the files to combine
    print('Enter the files you want to combine')
    filenames = list(tkinter.filedialog.askopenfilenames(filetypes = [('PDF Files', '*.pdf')]))
    if not filenames:
        print('No files selected')
        os._exit(1)

    print('Enter watermarking pdf');                                                            logging.debug(f'{filenames = }')
    watermarkPdf = tkinter.filedialog.askopenfilename(filetypes = [('PDF File', '*.pdf')])
    if not watermarkPdf:
        print('You didn\'t select a watermark')    

    # Encrypt the pdf using a user-input password
    password = pyip.inputPassword(prompt = 'Enter the password you want to encrypt the pdf with: ', blank = True) 

    # Sort the filenames so the pdfs are arranged in order
    filenames.sort();                                                                           logging.debug(f'Sorted {filenames = }'); logging.debug(f'{watermarkPdf = }')

    # Create the pdf file writer and watermark object
    output_pdf = pypdf2.PdfFileWriter()
    if watermarkPdf:
        watermark = pypdf2.PdfFileReader(open(watermarkPdf, 'rb')).getPage(0)

    # extract the entire text of the document
    docText = []
    # Add pages from the files 
    for filename in filenames:
        pdf = pypdf2.PdfFileReader(open(filename, 'rb'))
        # add custom watermark page
        for i in range(pdf.numPages):
            page = pdf.getPage(i);                                                              logging.info(f'Processing page {i + 1} of file {os.path.basename(filename)}')
            if watermarkPdf:
                page.mergePage(watermark)
            output_pdf.addPage(page)
            docText.append(page.extractText())     # keep the pages text

    # print document text
    print('The text in the document is: \n')
    print('\n'.join(docText).strip())
    print('\n', end = '')
    # encrypting and saving the output file
    saveAs = os.path.dirname(filenames[0]) + os.sep + 'output.pdf'
    if password == '':
        print('The pdf will be unprotected')
    else:
        output_pdf.encrypt(password)
        print('Document is secured with the entered password')
    outputfile = open(saveAs, 'wb');                                                            logging.info(f'{saveAs = }'); logging.info(f"Password blank: {password == ''}")
    output_pdf.write(outputfile)
    print('File saved as ' + saveAs)
    outputfile.close()


if __name__ == '__main__':
    main()
