# Download XKCD comics using multithreading
import tkinter.filedialog, threading, logging, time, os, sys
from ModuleImporter import module_importer
requests = module_importer('requests', 'requests')
bs4 = module_importer('bs4', 'beautifulsoup4')

# filename = 'multithreadedXKCD.log'
logging.basicConfig(level = logging.INFO, format = "%(asctime)s - %(levelname)s - %(lineno)d - %(message)s",
                    datefmt = '%d/%m/%Y - %I:%M:%S %p', filemode = 'w')
logging.disable(logging.CRITICAL)

# This is a constant value that should not be changed to avoid concurrency issues with threading
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
            print('Error downloading comic', comicNum, str(error));                             logging.error('Connection Error Comic #' + str(comicNum) + str(error))
            continue
        pageSoup = bs4.BeautifulSoup(page.text, 'lxml')
        imgTags = pageSoup.select('#comic img');                                                logging.debug(f'{imgTags = }')
        if not imgTags:
            print('Comic', comicNum, 'not found!');                                             logging.error('Not found Comic #' + str(comicNum))
            continue
        imgUrl = imgTags[0].get('src');                                                         logging.debug(f'{imgUrl = }')                      
        # download the image
        try:
            image = requests.get('https:' + imgUrl, headers = headers)
            image.raise_for_status()
        except Exception as err:
            print(str(err));                                                                    logging.error('Connection Error Comic #' + str(comicNum) + str(err))
            continue
        # save the downloaded file
        imageTitle = os.path.basename(imgUrl)
        saveName = os.path.join(directory, imageTitle);                                         logging.debug(f'{saveName = }')
        with open(saveName, 'wb') as imageFile:
            for chunk in image.iter_content(1000000):
                imageFile.write(chunk)
        print('Downloaded comic #' + str(comicNum), imageTitle)

def main():
    directory = tkinter.filedialog.askdirectory(title = 'Select download directory')
    if not directory:
        sys.exit('Download directory not chosen')
    directory = os.path.normpath(directory);                                                    logging.warning(f'{directory = }')
    
    # note the latest comic
    try:
        mainPage = requests.get('https://xkcd.com', headers = headers);                         logging.warning(f'{mainPage.status_code = }')
        mainPage.raise_for_status()
    except Exception as error:
        sys.exit(str(error))

    mainPageSoup = bs4.BeautifulSoup(mainPage.text, 'lxml')
    latestComicTag = mainPageSoup.select('#middleContainer > a:nth-child(6)');                  logging.info(f'{latestComicTag = }')
    try:
        latestComicLink = latestComicTag[0].get('href');                                        logging.info(f'{latestComicLink = }')
        latestComicNumber = int(latestComicLink[latestComicLink.rfind('/') + 1 : ]);            logging.info(f'{latestComicNumber = }')
    except IndexError:  # for latestComicLink
        sys.exit("Couldn't find the latest comic link")
    except ValueError:  # for latestComicNumber
        sys.exit('Unable to parse latest comic number')

    start_time = time.time()        # log start time
    # Initialize threading
    threads = []
    for end in range(latestComicNumber + 1, 0, -10):
        start = end - 10                                                                       
        if start < 1:
            start = 1
        logging.critical(f'{start = }, {end = }')
        downloadThread = threading.Thread(target = downloadXkcd, args = [start, end, directory])
        threads.append(downloadThread)
        downloadThread.start()      # starting thread
    
    # Pause until all the threads finish
    for thread in threads:
        thread.join()
    end_time = time.time()          # log finish time

    print('\nFinished downloading all the comics!')
    print('Total time taken = %.2f seconds' % (end_time - start_time))


if __name__ == '__main__':
    main()
