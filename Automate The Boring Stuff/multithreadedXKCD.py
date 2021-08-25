# Download XKCD comics using multithreading
import tkinter.filedialog, threading, logging, os, sys
from ModuleImporter import module_importer
requests = module_importer('requests', 'requests')
bs4 = module_importer('bs4', 'beautifulsoup4')

logging.basicConfig(filename = 'multithreadedXKCD.log', level = logging.INFO, format = "%(asctime)s - %(levelname)s - %(lineno)d - %(message)s",
                    datefmt = '%d/%m/%Y - %I:%M:%S %p', filemode = 'w')

# TODO: Add multithreading
# TODO: Add time logging

def downloadXkcd(startComic, endComic, directory):
    '''(int, int, str) -> None
    Download the a set of comics from startComic to endComic (exclusive)
    and save to given directory'''

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }

    for comicNum in range(startComic, endComic):
        # download the base page
        try:
            page = requests.get('https://xkcd.com/' + str(comicNum), headers = headers)
            page.raise_for_status()
        except Exception as error:
            print(str(error))
            continue
        pageSoup = bs4.BeautifulSoup(page.text, 'lxml')
        imgTag = pageSoup.select('#comic img')[0]
        imgUrl = imgTag.get('src')
        if not imgTag:
            print('No comic found!')
            continue
        # download the image
        try:
            image = requests.get('https:' + imgUrl, headers = headers)
            image.raise_for_status()
        except Exception as err:
            print(str(err))
            continue
        # write the downloaded file
        with open(os.path.join(directory, os.path.basename(imgUrl)), 'wb') as imageFile:
            for chunk in image.iter_content(1000000):
                imageFile.write(chunk)

def main():
    directory = tkinter.filedialog.askdirectory(title = 'Select download directory')
    if not directory:
        sys.exit('Download directory not chosen')
    directory = os.path.normpath(directory)

    
