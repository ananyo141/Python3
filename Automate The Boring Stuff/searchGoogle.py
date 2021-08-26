#!python3
# This program takes user input from the command line and searches the web for the keyword
# and displays the first 5 search results
import webbrowser, sys
from ModuleImporter import module_importer
googlesearch = module_importer('googlesearch', 'google')

if len(sys.argv) < 2:
    sys.exit("Usage: <script>.py {keyword to search}")

# Getting search keywords from the command line argument
keywords = (' ').join(sys.argv[1:])
try: 
    numResult = int(input("How many results you want to list?: "))
except ValueError:
    sys.exit("Invalid, expected integer input")

print(f"Searching Google for '{keywords}'...")
print(f"Listing {numResult} hits...")

searchResult = googlesearch.search(keywords, tld = 'co.in', num = numResult, stop = numResult, pause = 2)
for link in searchResult:
    webbrowser.open(link)
