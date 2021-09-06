# Send out remainders for the members of a group about their missed membership fees from a excel spreadsheet.

import tkinter.filedialog, smtplib, sys
from ModuleImporter import module_importer

openpyxl = module_importer('openpyxl', 'openpyxl')
pyip = module_importer('pyinputplus', 'pyinputplus')

def sendEmail(sender, recipient, **kwargs):
    ''' Send email from sender email address to recipient email address 
    Supported keyword arguments:
    password, subject, content for respective purposes (each set to None by default '''
    password = kwargs.get('password', None)
    subject = kwargs.get('subject', None)
    content = kwargs.get('content', None)

    if password == None:
        password = pyip.inputPassword(f'Enter password for mail {sender}: ')
    if subject == None:
        subject = input("Enter subject of email")
    if content == None:
        content = input("Enter content of email")
    
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587) # potential smtplib.socket.gaierror
    smtpObj.ehlo()      # saying hello to server
    smtpObj.starttls()  # start encryption protocol
    smtpObj.login(sender, password)  # potential smtplib.SMTPAuthenticationError
    
    status = smtpObj.sendmail(sender, recipient, f"Subject: {subject}\n{content}")

    smtpObj.quit()  # end the connection
    return status


# TODO: Ask the user for membership file  
# TODO: Read the file for all the members who have not paid
# TODO: send customized messages for them



def main():
    membershipFile = tkinter.filedialog.askopenfilename(filetypes = [('Excel Spreadsheet', '*.xlsx')])
    senderEmail = pyip.inputEmail("Enter sender email: ")
    password = pyip.inputPassword(f"Enter password for {senderEmail}: ")
    
    xlFile = openpyxl.load_workbook(membershipFile)
    xlSheet = xlFile.active

    # Find the members who have not paid their dues
    for rowNum in range(2, xlSheet.max_row + 1): # first row contains headings and month names
        for colNum in range(3, xlSheet.max_column + 1): # first two columns contain name and email details
            monthsDue = []
            if xlSheet.cell(row = rowNum, column = colNum).value != 'paid':
                defaultedMonth = xlSheet.cell(row = 1, column = colNum).value
                monthsDue.append(defaultedMonth)
            if not monthsDue:
                continue    # if no months were due

            # send the personalized email
            defaulterName = xlSheet.cell(row = rowNum, column = 1).value
            recipientEmail = xlSheet.cell(row = rowNum, column = 2).value

            message = (f"Hey {defaulterName}, this is to inform you that " 
                        f"we still haven't got your payment for the month of "
                        f"{', '.join(monthsDue)} and since we are on a tight budget, "
                        "it will be super helpful if you can settle the due within "
                        "the end of this month. Looking forward to meet you!\n\nAni.")
            try:
                status = sendEmail(senderEmail, recipientEmail,
                            password = password, subject = "Fees Due", content = message)
            except smtplib.socket.gaierror:
                sys.exit("Unable to connect to gmail smpt server")
            except smtplib.SMTPAuthenticationError:
                sys.exit(f"Invalid email or password provided\n"
                    "Tip: Make sure you have 'unsecured app access' enabled in your Gmail settings")
            if status != {}:
                print("Error sending email")
            else:
                print(f"Email sent to {recipientEmail} for due month {', '.join(monthsDue)}...")                

    print("Emails were sent to the defaulters")


if __name__ == '__main__':
    main()
