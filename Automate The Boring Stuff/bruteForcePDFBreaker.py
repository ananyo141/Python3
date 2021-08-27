# Brute force break the password of user pdf
import tkinter.filedialog, multiprocessing, sys
from ModuleImporter import module_importer
pypdf2 = module_importer('PyPDF2', 'PyPDF2')

passFound = []

def bruteForce(passwords: list, start: int, stop: int, pdfPath: str) -> None:
    '''Try to decrypt an encrypted pdf and return status in a global variable "Cracked" '''
    global passFound
    if passFound:     # return if already cracked
        return
    encryptedFile = open(pdfPath, 'rb')
    encryptedPdf = pypdf2.PdfFileReader(encryptedFile)
    if not encryptedPdf.isEncrypted:
        sys.exit('PDF is unencrypted')
    
    # check every word, uppercase and lowercase
    for i in range(start, stop):
        if passFound:
            break
        word = passwords[i].strip()
        print(f'Trying pass: {word}')
        if encryptedPdf.decrypt(word.lower()):
            print(f'Password cracked: {word.lower()}')
            # global Cracked
            passFound.append(word.lower())
            print(passFound)
            break
        elif encryptedPdf.decrypt(word.upper()):
            print(f'Password cracked: {word.upper()}')
            passFound.append(word.upper())
            break
    encryptedFile.close()

def main():
    # Input the dictionary file
    try:
        possiblePass = tkinter.filedialog.askopenfile(title = 'Input dictionary file', filetypes = [('Text Files','*.txt')]).readlines()
    except ArithmeticError:
        sys.exit('Possible list of passwords not given')
    # Input the encrypted file
    encryptedFile = tkinter.filedialog.askopenfilename(title = 'Input encrypted file', filetypes = [('PDF Files','*.pdf')])
    if not encryptedFile:
        sys.exit('Encrypted pdf not specified')
    
    print('Commencing Brute Force Attack')

    processes = []
    manager = multiprocessing.Manager()
    pa = manager.dict()
    # take start matching from end to tackle non-multiple indexes of 12
    for end in range(len(possiblePass), 0, -12):
        start = end - 12;          
        if start < 0:
            start = 0

        process = multiprocessing.Process(target = bruteForce, args = [possiblePass, start, end, encryptedFile])
        processes.append(process)
        process.start()

    # wait for every process to finish
    for process in processes:
        process.join()

    print(passFound)

    if passFound:
        print('Pdf password successfully cracked')
    else:
        print('Pdf could not be decrypted')

if __name__ == '__main__':
    main()
