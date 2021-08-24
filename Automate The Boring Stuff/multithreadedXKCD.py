# Download XKCD comics using multithreading
import threading, logging, sys, os
from ModuleImporter import module_importer
requests = module_importer('requests', 'requests')
bs4 = module_importer('bs4', 'beautifulsoup4')

logging.basicConfig(filename = 'multithreadedXKCD.log', level = logging.DEBUG, format = "%(asctime)s - %(levelname)s - %(lineno)d - %(message)s",
                    datefmt = '%d/%m/%Y - %I:%M:%S %p', filemode = 'w')

# TODO: Add multithreading
# TODO: Add time logging

def downloadXkcd(startComic, endComic, directory):
    '''(int, int) -> None
    Download the a set of comics from startComic to endComic (non-inclusive)
    and save to given directory'''

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }

    for comicNum in range(startComic, endComic):
        try:
            page = requests.get('https://xkcd.com/' + comicNum, headers = headers)
            page.raise_for_status()
        except Exception as error:
            sys.exit(str(error))
        pageSoup = bs4.BeautifulSoup(page.text, 'lxml')
        

