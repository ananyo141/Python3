# Download torrent link remotely when sent by ananyo141@gmail.com
import tkinter.filedialog, imaplib, subprocess, datetime, time, logging, sys, os
from emailDues import sendEmail
from ModuleImporter import module_importer
imaplib._MAXLINE = 10000000

imapclient = module_importer('imapclient', 'imapclient')
pyzmail = module_importer('pyzmail', 'pyzmail')
pyip = module_importer('pyinputplus', 'pyinputplus')

logging.basicConfig(level = logging.INFO, format = '%(asctime)s - %(levelname)s - %(lineno)d - %(message)s',
                    datefmt = '%d/%m/%Y %I:%M:%S %p') # filename = 'remoteTorrent.log', filemode = 'w'
logging.disable(logging.CRITICAL)

def getDate() -> str:
    ''' Return the current date formatted like 01-Jan-2001 '''
    now = datetime.datetime.now()
    return now.strftime('%d-%b-%Y')

def main():
    # ask user to enter bittorrent-client executable path
    torrentClientPath = tkinter.filedialog.askopenfilename(title = 'Enter torrent client executable');  logging.info(f'{torrentClientPath = }')
    if not torrentClientPath:
        sys.exit("No torrent client selected")
    # ask user for watch email and password
    watchEmail = pyip.inputEmail("Enter the email to monitor: ");                                       logging.info(f'{watchEmail = }')
    watchPassword = pyip.inputPassword("Enter password: ");                                             logging.info(f'Watch Password Entered {watchPassword != ""}')
    # ask for authenticated email(from which will accept commands)
    authEmail = pyip.inputEmail("Enter superuser email address to accept commands: ");                  logging.info(f'{authEmail = }')
    print(os.path.basename(torrentClientPath), "selected as torrent client...")

    searchDate = getDate();                                                                             logging.info(f'{searchDate = }')
    # log in email and check for command every 15 mins
    with imapclient.IMAPClient('imap.gmail.com', ssl = True) as imapObj:
        print(f"Logging in {watchEmail}")
        try:
            imapObj.login(watchEmail, watchPassword)
        except imapclient.exceptions.LoginError:
            sys.exit('\nInvalid login credentials\n'
                     'Tip: Ensure you have "unsecured app access" enabled in your google security settings')
        imapObj.select_folder('INBOX', readonly = False)
        while True:
            print(f'Searching for emails from {authEmail}')
            UIDs = imapObj.search([b'SINCE', searchDate.encode(), b'FROM', authEmail.encode()]);       logging.info(f'{UIDs = }')
            rawMessages = imapObj.fetch(UIDs, ['BODY[]', 'FLAGS'])
            commandFound = False

            for uid in UIDs:
                message = pyzmail.PyzMessage.factory(rawMessages[uid][b'BODY[]']);                     logging.info(f'{message.get_subject().lower() = }')
                if message.get_subject().lower() == 'sudo python':      # a passcode in subject for authentication from authEmail
                    commandFound = True
                    print("Command recieved and authenticated")
                    # extract torrent link
                    magnetLink = message.text_part.get_payload().decode(message.text_part.charset).strip();    logging.info(f'{magnetLink = }')
                    if magnetLink.lower() == 'stop':
                        print("Exiting...")
                        # delete the stop mail
                        imapObj.delete_messages(uid)
                        imapObj.expunge()
                        sys.exit(0)
                    print(f'Sending confirmation email to {authEmail} and starting download')
                    # if command found, email starting download
                    sendEmail(watchEmail, authEmail, f'Starting download of magnet link', 
                                subject = 'RemoteTorrent', password = watchPassword)
                    # open torrent client with link and wait for completion
                    subprocess.Popen([torrentClientPath, magnetLink]).wait()
                    print("Download completed.")
                    # send download successful message
                    sendEmail(watchEmail, authEmail, f'Completed download of magnet link',
                              subject = 'RemoteTorrent', password = watchPassword)

                    print('Deleting completed command email...')
                    # delete mail
                    imapObj.delete_messages(uid)
                    imapObj.expunge()
            if not commandFound:
                print("Command not given, sleeping for 15 minutes")
                time.sleep(30)     # otherwise sleep for 15 minutes before checking again
            imapObj.noop()         # reload for new email commands
            print('Reloading inbox...\n')

if __name__ == '__main__':
    main()
