# Unsubscribe from all the pesky emails with one click

import imaplib, webbrowser
from ModuleImporter import module_importer

imaplib._MAXLINE = 10000000     # set a higher size limit for fetching email messages

pyip = module_importer('pyinputplus', 'pyinputplus')
bs4 = module_importer('bs4', 'beautifulsoup4')
pyzmail = module_importer('pyzmail', 'pyzmail36==1.0.4')
imapclient = module_importer('imapclient', 'imapclient')

def main():
    userEmail = pyip.inputEmail(prompt = "Enter your gmail: ")                      # enter mail
    password = pyip.inputPassword(prompt = f"Enter password for '{userEmail}': ")   # enter password
    
    with imapclient.IMAPClient('imap.gmail.com', ssl = True) as imapObj:    # start connection (handles abrupt connection drop)
        imapObj.login(userEmail, password)                                  # login with given email and password
        imapObj.select_folder('INBOX', readonly = True)                     # select the inbox folder with readonly mode (can't delete or make changes)
        allMessageUIDs = imapObj.search()                                   # get all the message unique ids
        rawMessages = imapObj.fetch(allMessageUIDs, ['BODY[]', 'FLAGS'])    # download all the messages
        for UID in allMessageUIDs:                                          
            message = pyzmail.PyzMessage.factory(rawMessages[UID][b'BODY[]']) # parse each message
            try:
                messageHtmlPart = message.html_part.get_payload().decode(message.html_part.charset) # separate the html part
            except AttributeError:                                          # if mail has no html part
                continue
            messageSoup = bs4.BeautifulSoup(messageHtmlPart, 'lxml')        # parse the html part
            linkTags = messageSoup.select('a')                              # get all the links
            for linkTag in linkTags:
                linkText = linkTag.getText().lower()
                if 'unsubscribe' in linkText or linkText == 'click here':   # if unsubscribe or 'click here' is a part of link text,
                    link = linkTag.get('href')
                    print(f'\nFound unsubscribe link: {link}')               
                    try:
                        webbrowser.open(link)                               # open the link in browser tab
                    except Exception as exc:
                        print(f'Unable to open {link}, {str(exc)}')
        
    print("Successfully unsubscribed from all newsletters")


if __name__ == '__main__':
    main()
