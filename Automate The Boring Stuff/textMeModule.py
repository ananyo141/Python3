import os
from ModuleImporter import module_importer

twilio = module_importer('twilio', 'twilio')
from twilio.rest import Client

def textTo(number: str, message: str) -> None:
    ''' Send a message to the given number using twilio module and preset 
    authorization tokens in the environment variables '''

    # get preset values from the os environment variables with these names:
    accountSID = os.environ.get('accountSID')
    authToken = os.environ.get('authToken')
    twilioNumber = os.environ.get('twilioNumber')

    twilioCli = Client(accountSID, authToken)
    twilioCli.messages.create(body = message, from_ = twilioNumber, to = number)
