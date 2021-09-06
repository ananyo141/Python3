######################################################################################
#                                                                                    #  
#   GOOGLE has started providing new features (like, OAuth) that prevents scripts    #                                                                             
#   from using selenium to sign-in. Other vendors like yahoo also enforce            #                                                                          
#   captcha, and automated email services also require some form of authentication.  #                                                                                    
#                                                                                    #  
######################################################################################                                                                                      

# Send an email with the help of Selenium
import tkinter.filedialog, smtplib, textwrap, datetime, sys, os
from ModuleImporter import module_importer

pyip = module_importer('pyinputplus', 'pyinputplus')

def timestamp():
    ''' Capture the device date and time information and return the formatted string '''
    now = datetime.datetime.now()
    return now.strftime("%a %b %d, %Y %I:%M:%S %p")

def main():
    
    # ask for recipient address
    recipient = pyip.inputEmail(prompt = "Enter Recipient Email: ")
    # ask for email subject and body (give option to select a text file)
    subject = input("Enter subject: ")
    choice = pyip.inputMenu(['Enter text by typing', 'Enter from a text file'],
                             prompt = 'Email Body:\n', numbered = True)
    if choice.lower() == 'enter text by typing':
        content = input("Enter the body of email:\n")
    elif choice.lower() == 'enter from a text file':
        content = tkinter.filedialog.askopenfile(filetypes = [('Text', '*.txt')], mode = 'r').read()
    
    # ask for sender email, password
    sender = pyip.inputEmail(prompt = "Enter your email: ")
    password = pyip.inputPassword(prompt = f'Enter gmail account password for {sender}: ')

    # initialize the wapper object to write wrapped text
    wrapper = textwrap.TextWrapper(width = 70)

    # save draft in case of failure
    with open('./draft.txt', mode = 'w') as draft:
        draft.write(f'To: {recipient}\n\n')
        draft.write(f'Subject: {wrapper.fill(text = subject)}'.center(100) + '\n\n')
        draft.write(wrapper.fill(text = content) + '\n')
        draft.write(f'From: {sender}'.rjust(100) + '\n')
        draft.write(timestamp().rjust(100))

    # fill in the information and send the email and close connection
    # start connection
    try:
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    except smtplib.socket.gaierror:
        sys.exit("Unable to connect to gmail smtp server")
    
    smtpObj.ehlo()        # say hello to the server (identify script)
    smtpObj.starttls()    # start encryption mode
    try:
        smtpObj.login(sender, password)
    except smtplib.SMTPAuthenticationError:
        sys.exit(f"Invalid email or password provided. Draft saved at {os.getcwd()}\n"
            "Tip: Make sure you have 'unsecured app access' enabled in your Gmail settings")

    smtpObj.sendmail(sender, recipient, f"Subject: {subject}\n{content}")

    choice = pyip.inputYesNo(prompt = "Email sent. Do you want to delete the draft?: ")
    if choice.lower() == "yes":
        os.unlink('draft.txt')
    else:
        print("Draft saved at '%s'\n" % (os.getcwd()))

    smtpObj.quit() # ending connection


if  __name__ == '__main__':
    main()
