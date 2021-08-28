# Brute force break the password of user pdf
import tkinter.filedialog, multiprocessing, sys, time
from ModuleImporter import module_importer
pypdf2 = module_importer('PyPDF2', 'PyPDF2')

def bruteForce(passwords: list, start: int, stop: int, pdfPath: str, maintainer: multiprocessing.Manager) -> None:
    ''' Try to decrypt an encrypted pdf and save password in process manager '''
    encryptedFile = open(pdfPath, 'rb')
    encryptedPdf = pypdf2.PdfFileReader(encryptedFile)
    if not encryptedPdf.isEncrypted:
        sys.exit('PDF is unencrypted')
    
    # check every word, uppercase and lowercase
    for i in range(start, stop):          # stop is non-inclusive
        if maintainer:
            break
        word = passwords[i].strip()
        print(f'Trying pass: {word}')
        if encryptedPdf.decrypt(word.lower()):
            maintainer['Password'] = word.lower()
            break
        elif encryptedPdf.decrypt(word.upper()):
            maintainer['Password'] = word.upper()
            break

    encryptedFile.close()

def main():
    # Input the dictionary file
    try:
        possiblePass = tkinter.filedialog.askopenfile(title = 'Input dictionary file',
                        filetypes = [('Text Files','*.txt')]).readlines()
    except AttributeError:
        sys.exit('Possible list of passwords not given')
    # Input the encrypted file
    encryptedFile = tkinter.filedialog.askopenfilename(title = 'Input encrypted file',
                        filetypes = [('PDF Files','*.pdf')])
    if not encryptedFile:
        sys.exit('Encrypted pdf not specified')
    
    print('Commencing Brute Force Attack')

    processes = []
    manager = multiprocessing.Manager()   # processes manager (shared variable: dict) that,
    maintainer = manager.dict()           # communicates status between the processes.
    start_time = time.time()              # mark start time
    # Create 12 processes, each tackling len(possiblePass) / 12 passwords
    NUM_PROCESSES = 12                    # constant processess to be executed
    passwordsPerProcess = int(len(possiblePass) / NUM_PROCESSES)

    for start in range(0, len(possiblePass) + 1, passwordsPerProcess):
        end = start + passwordsPerProcess;          
        if end > len(possiblePass):       # if end out of bounds,
            end = len(possiblePass)       # reset to last valid index

        process = multiprocessing.Process(target = bruteForce, args = [possiblePass, start, end, encryptedFile, maintainer])
        processes.append(process)
        process.start()

    # join child processes in main process
    for process in processes:
        process.join()

    end_time = time.time()                # mark end time
    
    if maintainer:
        print(f"\nPdf password cracked '{maintainer['Password']}' in {round(end_time - start_time, 2)} seconds")
    else:
        print('Pdf could not be decrypted')

if __name__ == '__main__':
    main()
