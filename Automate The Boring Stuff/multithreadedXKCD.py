# Download XKCD comics using multithreading
import tkinter.filedialog, threading, logging, os, sys
from ModuleImporter import module_importer
requests = module_importer('requests', 'requests')
bs4 = module_importer('bs4', 'beautifulsoup4')

logging.basicConfig(filename = 'multithreadedXKCD.log', level = logging.INFO, format = "%(asctime)s - %(levelname)s - %(lineno)d - %(message)s",
                    datefmt = '%d/%m/%Y - %I:%M:%S %p', filemode = 'w')

# TODO: Add multithreading
# TODO: Add time logging

# This is a constant value that should not change to avoid concurrency issues with threading
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
}

def downloadXkcd(startComic, endComic, directory):
    '''(int, int, str) -> None
    Download the a set of comics from startComic to endComic (exclusive)
    and save to given directory'''

    for comicNum in range(startComic, endComic):
        # download the base page
        try:
            page = requests.get('https://xkcd.com/' + str(comicNum), headers = headers);        logging.info(f'{page.status_code = }')
            page.raise_for_status()
        except Exception as error:
            print(str(error))
            continue
        pageSoup = bs4.BeautifulSoup(page.text, 'lxml');                                        logging.debug(f'{pageSoup = }')
        imgTags = pageSoup.select('#comic img');                                                logging.info(f'{imgTags = }')
        if not imgTags:
            print('No comic found!')
            continue
        imgUrl = imgTags[0].get('src');                                                         logging.info(f'{imgUrl = }')                      
        # download the image
        try:
            image = requests.get('https:' + imgUrl, headers = headers)
            image.raise_for_status()
        except Exception as err:
            print(str(err))
            continue
        # write the downloaded file
        saveName = os.path.join(directory, os.path.basename(imgUrl));                           logging.critical(f'{saveName = }')
        with open(saveName, 'wb') as imageFile:
            for chunk in image.iter_content(1000000):
                imageFile.write(chunk)

def main():
    directory = tkinter.filedialog.askdirectory(title = 'Select download directory')
    if not directory:
        sys.exit('Download directory not chosen')
    directory = os.path.normpath(directory);                                                    logging.critical(f'{directory = }')
    
    # note the latest comic
    try:
        mainPage = requests.get('https://xkcd.com', headers = headers);                         logging.critical(f'{mainPage.status_code = }')
        mainPage.raise_for_status()
    except Exception as error:
        sys.exit(str(error))

    mainPageSoup = bs4.BeautifulSoup(mainPage.text, 'lxml');                                    logging.debug(f'{mainPageSoup = }')
    latestComicTag = mainPageSoup.select('#middleContainer > a:nth-child(6)');                  logging.info(f'{latestComicTag = }')
    try:
        latestComicLink = latestComicTag[0].get('href');                                        logging.info(f'{latestComicLink = }')
        latestComicNumber = int(latestComicLink[latestComicLink.rfind('/') + 1 : ]);            logging.info(f'{latestComicNumber = }')
    except IndexError:  # for latestComicLink
        sys.exit("Couldn't find the latest comic link")
    except ValueError:  # for latestComicNumber
        sys.exit('Unable to parse latest comic number')

    # initialize threading
    threads = []
    for start in range(latestComicNumber, 0, -10):
        end = start - 10
        if end < 1:
            end = 1
        
        downloadThread = threading.Thread(target = downloadXkcd, args = [end, start, directory])
        threads.append(downloadThread)
        downloadThread.start()      # start the thread
    
    # pause until all the threads finish
    for thread in threads:
        thread.join()

    print('Finished downloading all the comics!')


if __name__ == '__main__':
    main()
