#!python3
# This program uses the command line to open the map of a particular location from the terminal
import webbrowser, sys, logging
logging.basicConfig(level = logging.DEBUG, format  = ' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

address = ('+').join(sys.argv[1:])
logging.debug(f'{address=}')
webbrowser.open("https://www.google.com/maps/place/" + address)