import os
from ModuleImporter import module_importer

twilio = module_importer('twilio', 'twilio')
from twilio.rest import Client

def textTo(number: str, message: str) -> None:
    ''' Send a message to the given number using twilio module and preset 
    authorization tokens in the environment variables '''

    # get preset values from the os environment variables with these names:
    accountSID = os.environ.get('accountSID')   # twilio account SID
    authToken = os.environ.get('authToken')  # twilio authorizaton token
    twilioNumber = os.environ.get('twilioNumber') # number provided by twilio to send text

    if not accountSID:
        raise Exception("Environment variable for accountSID not set")
    if not authToken:
        raise Exception("Environment variable for authToken not set")
    if not twilioNumber:
        raise Exception("Environment variable for twilioNumber not set")

    twilioCli = Client(accountSID, authToken)
    twilioCli.messages.create(body = message, from_ = twilioNumber, to = number)
