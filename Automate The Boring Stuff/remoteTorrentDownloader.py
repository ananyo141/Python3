# Download torrent link remotely when sent by ananyo141@gmail.com
import tkinter.filedialog, imapclient, imaplib, pyzmail, subprocess, datetime, time, logging, pyinputplus as pyip, sys
from emailDues import sendEmail
imaplib._MAXLINE = 10000000

logging.basicConfig(level = logging.INFO, format = '%(asctime)s - %(levelname)s - %(lineno)d - %(message)s',
                    datefmt = '%d/%m/%Y %I:%M:%S %p', filename = 'remoteTorrent.log', filemode = 'w')

def getDate() -> str:
    ''' Return the current date formatted as 01-Jan-2001 '''
    now = datetime.datetime.now()
    return now.strftime('%d-%b-%Y')

def main():
    # ask user to enter bittorrent client executable path
    torrentClientPath = tkinter.filedialog.askopenfilename(title = 'Enter torrent client executable')
    if not torrentClientPath:
        sys.exit("No client selected")
    # ask user for watch email
    watchEmail = pyip.inputEmail("Enter the email to monitor: ")
    # ask user for watch password
    watchPassword = pyip.inputPassword("Enter password: ")
    # ask for authenticated email(from which will accept commands)
    authEmail = pyip.inputEmail("Enter superuser email address to accept commands: ")

    searchDate = getDate()
    # log in email and check for command every 15 mins
    imapObj = imapclient.IMAPClient('imap.gmail.com', ssl = True)
    imapObj.login(watchEmail, watchPassword)
    imapObj.select_folder('INBOX', readonly = False)
    while True:
        UIDs = imapObj.search([b'SINCE', searchDate.encode(), b'FROM', authEmail.encode()])
        rawMessages = imapObj.fetch(UIDs, ['BODY[]', 'FLAGS'])
        commandFound = False
        killSwitch = False

        for uid in UIDs:
            message = pyzmail.PyzMessage.factory(rawMessages[uid][b'BODY[]'])
            if message.get_subject().lower() == 'sudo python':      # a passcode for authentication
                commandFound = True
                magnetLink = message.text_part.get_payload().decode(message.text_part.charset)
                if magnetLink.lower() == 'stop':
                    killSwitch = True
                    break
                subprocess.Popen([torrentClientPath, magnetLink]).wait()
                imapObj.delete_messages(uid)
                imapObj.expunge()
        if not commandFound:
            time.sleep(15 * 60)
        if killSwitch:
            break


    # TODO: if command found, email starting download
    # TODO: extract torrent link
    # TODO: open torrent client with link and wait for completion
    # TODO: delete mail
    # TODO: send download successful message

if __name__ == '__main__':
    main()
