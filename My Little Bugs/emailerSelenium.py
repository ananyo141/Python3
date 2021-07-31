######################################################################################
#                                                                                    #  
#   GOOGLE has started providing new features (like, OAuth) that prevents scripts    #                                                                             
#   from using selenium to sign-in. Other vendors like yahoo also enforce            #                                                                          
#   captcha, and automated email services also require some form of authentication.  #                                                                                    
#                                                                                    #  
######################################################################################                                                                                      

# Send an email with the help of Selenium
import tkinter.filedialog, pyinputplus as pyip, datetime, sys
from selenium import webdriver

# TODO: ask for the gecko driver
# TODO: ask for recipient address
# TODO: ask for email subject and body (give option to select a text file)
# TODO: ask for sender email
# TODO: save draft and delete if send successful
# TODO: ask for sender password
# TODO: fill in the information and send the email and log out

def timestamp():
    now = datetime.datetime.now()
    return f'{now.strftime("%a")} {now.strftime("%b")} ' \
        f'{now.strftime("%d")}, {now.strftime("%Y")} {now.strftime("%l")}:'\
        f'{now.strftime("%M")}:{now.strftime("%S")} {now.strftime("%p")}'

def main():
    print("Select the gecko driver for Mozilla Firefox:")
    gecko = tkinter.filedialog.askopenfilename()
    if not gecko:
        sys.exit("Gecko driver not selected")
    
    recipient = pyip.inputEmail(prompt = "Enter Recipient Email: ")
    subject = input("Enter subject: ")
    choice = pyip.inputMenu(['Enter text by typing', 'Enter from a text file'], prompt = 'Email Body:\n', numbered = True)
    if choice.lower() == 'enter text by typing':
        content = input("Enter the body of email:\n")
    elif choice.lower() == 'enter from a text file':
        content = tkinter.filedialog.askopenfile(filetypes = [('Text', '.txt')], mode = 'r').read()
    
    sender = pyip.inputEmail(prompt = "Enter Sender email: ")

    # save draft in case of failure
    draft = open('./draft.txt', mode = 'w')
    draft.write(f'To: {recipient}\n\n')
    draft.write(f'Subject: {subject}'.center(100) + '\n\n')
    draft.write(content + '\n')
    draft.write(f'From: {sender}'.rjust(100) + '\n')
    draft.write(timestamp().rjust(100))
    draft.close()

    password = pyip.inputPassword(prompt = f'Enter gmail account password for {sender}: ')

    # Send email with Selenium
    browser = webdriver.Firefox(executable_path = gecko)
    browser.get('https://accounts.google.com/ServiceLogin?service=mail')
    userElem = browser.find_element_by_id('identifierId')
    userElem.send_keys(sender)
    nextElem = browser.find_element_by_css_selector('.VfPpkd-LgbsSe-OWXEXe-k8QpJ > span:nth-child(3)')
    nextElem.submit()



if  __name__ == '__main__':
    main()
