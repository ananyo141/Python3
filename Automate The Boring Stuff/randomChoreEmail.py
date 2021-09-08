# Assign random chore to a bunch of emails
import random, smtplib, logging, sys
from emailDues import sendEmail
from ModuleImporter import module_importer

pyip = module_importer('pyinputplus', 'pyinputplus')
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(lineno)d - %(message)s",
                    datefmt="%d/%m/%Y %I:%M:%S %p")  # filename = 'randomChoreEmail.log', filemode = 'w'
logging.disable(logging.CRITICAL)

def main():
    senderEmail = pyip.inputEmail("Enter sender email: ");                  logging.info(f'{senderEmail = }')
    password = pyip.inputPassword(f"Enter password for '{senderEmail}': ")

    chores = ['dishes', 'bathroom', 'vacuum', 'walk dog']
    emails = input(f"Enter {len(chores)} emails: ")
    emails = [email.strip() for email in emails.split(',')];                logging.info(f'{emails = }')

    for email in emails:
        choreAssigned = random.choice(chores);                              logging.info(f'{choreAssigned = }')
        if email == '':
            continue
        
        try:
            sendEmail(senderEmail, email, content = f'Hey {email}, your chore is {choreAssigned}\n',
                      password = password, subject = 'Chore of the Week')
        except smtplib.socket.gaierror:
            sys.exit("Unable to connect to gmail smpt server")
        except smtplib.SMTPAuthenticationError:
            sys.exit(f"Invalid email or password provided\n"
                    "Tip: Make sure you have 'unsecured app access' enabled in your Gmail settings")

        print(f"Successfully sent chore '{choreAssigned}' to {email}")
        chores.remove(choreAssigned)

    logging.info(f'{chores = }')
    if chores:
        print("Chores still unassigned:")
        for chore in chores:
            print(chore)

if __name__ == '__main__':
    main()
