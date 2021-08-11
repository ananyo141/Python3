import tkinter.filedialog, sys, os
from ModuleImporter import module_importer
pypdf2 = module_importer('PyPDF2', 'PyPDF2')
pyip = module_importer('pyinputplus', 'pyinputplus')

def main():
    pdfFilename = tkinter.filedialog.askopenfilename(filetypes = [('PDF Files','*.pdf')])
    if not pdfFilename:
        sys.exit('No files chosen')
    passw = pyip.inputPassword(prompt = 'Enter the password to encrypt with: ')
    pdfFile = pypdf2.PdfFileReader(open(pdfFilename, 'rb'))
    pdfWriter = pypdf2.PdfFileWriter()
    for i in range(pdfFile.numPages):
        pdfWriter.addPage(pdfFile.getPage(i))
    with open(os.path.join(os.path.dirname(pdfFilename), 'encrypted_' + os.path.basename(pdfFilename)), 'wb') as savePdf:
        pdfWriter.encrypt(passw)
        pdfWriter.write(savePdf)
    print('Successfully saved encrypted pdf')

if __name__ == '__main__':
    main()
