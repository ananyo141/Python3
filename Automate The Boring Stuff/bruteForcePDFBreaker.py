# Brute force break the password of user pdf
import tkinter.filedialog, sys
from ModuleImporter import module_importer
pypdf2 = module_importer('PyPDF2', 'PyPDF2')

def main():
    # Input the dictionary file
    possiblePass = tkinter.filedialog.askopenfile(filetypes = [('Text Files','*.txt')]).readlines()
    if not possiblePass:
        sys.exit('Possible list of passwords not given')
    # Input the encrypted file
    encryptedFile = tkinter.filedialog.askopenfile(filetypes = [('PDF Files','*.pdf')], mode = 'rb')
    if not encryptedFile:
        sys.exit('Encrypted pdf not specified')
    encryptedPdf = pypdf2.PdfFileReader(encryptedFile)
    if not encryptedPdf.isEncrypted:
        sys.exit('PDF unencrypted')
    print('Commencing Brute Force Attack')
    # Check every word, uppercase and lowercase
    for word in possiblePass:
        word = word.strip()
        print(f'Trying pass: {word}')
        if encryptedPdf.decrypt(word.lower()):
            print(f'Password cracked: {word.lower()}')
            break
        elif encryptedPdf.decrypt(word.upper()):
            print(f'Password cracked: {word.upper()}')
            break
    try:
        encryptedPdf.getPage(0)
        print('Pdf password successfully cracked')
    except:
        print('Pdf could not be decrypted')

if __name__ == '__main__':
    main()
