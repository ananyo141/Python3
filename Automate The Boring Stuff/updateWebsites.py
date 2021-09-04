#!/usr/bin/python3
# This script goes online and searches for the latest comics from a bunch of websites and 
# downloads them if not already downloaded.

    # List of Websites  #
# http://www.lefthandedtoons.com/
# https://www.buttersafe.com/
# https://www.savagechickens.com/
# http://www.lunarbaboon.com/
# https://www.exocomics.com/
# http://nonadventures.com/
# https://moonbeard.com/    
# http://www.happletea.com/     # not responsive right now


import tkinter.filedialog, threading, logging, pprint, sys, os
from ModuleImporter import module_importer

requests = module_importer('requests', 'requests')
bs4 = module_importer('bs4', 'beautifulsoup4')

logging.basicConfig(level = logging.ERROR, format = "%(asctime)s - %(levelname)s - %(lineno)d - %(message)s",
                    datefmt = "%d/%m/%Y %I:%M:%S %p", filename = "updateWebsites.log", filemode = "w")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
}

# create classes and methods for each website

class LeftHandedToons:
    latestComicNum = None

    def __init__(self):
        self.comicDownloaded = 0
        # initialize once during creation of first object instance
        if LeftHandedToons.latestComicNum == None:
            LeftHandedToons.fetchLatestComicNum()

    # Download comics 
    def downloadComics(self, downloadDir, **kwargs):
        '''Download comic to the given downloadDir according to given arguments
        with threading support

        Support optional keyword arguments:
        startComic = (1 by default), 
        endComic = (latestComicNum + 1 by default)
        '''

        # nested target function
        def downloadComicSq(downloadDir, start, stop):
            ''' Download comics sequentially, this is going to be the target function for threading '''

            saveDir = os.path.join(downloadDir, 'LeftHandedToons')
            os.makedirs(saveDir, exist_ok = True)
            for pageNum in range(start, stop):
                pageLink = f"http://www.lefthandedtoons.com/{pageNum}/";                        logging.info(f"{start = }, {stop = }")
                try:
                    page = requests.get(pageLink, headers = headers)
                    page.raise_for_status();                                            logging.warning(f"{page.status_code = }")
                except Exception as exc:
                    print(f"Unable to download comic #{pageNum}");                       logging.error(f"{pageLink = }\n{pprint.pformat(str(exc))}")
                    continue
                pageSoup = bs4.BeautifulSoup(page.text, 'lxml')
                try:
                    imgLink = pageSoup.select('#comicwrap > div.comicdata > img')[0].get('src');        logging.warning(f"{imgLink = }")
                except IndexError:
                    print(f"Unable to find image for comic #{pageNum}");                       logging.error(f"{pageNum = }")
                    continue
                print(f"Downloading {os.path.basename(imgLink)}...")
                # download image
                try:
                    image = requests.get(imgLink, headers = headers);                           logging.warning(f"{image.status_code = }")
                    image.raise_for_status()
                except Exception as exc:
                    print(f"Error saving comic #{pageNum}");                       logging.error(f"{pageLink = }\n{pprint.pformat(str(exc))}")
                    continue

                imageFileName = os.path.join(saveDir, os.path.basename(imgLink))
                with open(imageFileName, 'wb') as imageFile:
                    for chunk in image.iter_content(1000000):
                        imageFile.write(chunk)

                self.comicDownloaded += 1


        # Initialize start and stop
        startComic = kwargs.get('startComic', 1)   # comic range starts from 1
        stopComic  = kwargs.get('endComic', LeftHandedToons.latestComicNum + 1)  # since stop is non-inclusive

        comicPerThread = 10
        threads = []    # thread buffer
        for start in range(startComic, stopComic, comicPerThread):
            stop = start + comicPerThread
            if stop > stopComic:
                stop = stopComic

            downloadThread = threading.Thread(target = downloadComicSq, args = [downloadDir, start, stop])
            threads.append(downloadThread)
            downloadThread.start()

        # wait for downloads
        for thread in threads:
            thread.join()

    @classmethod
    def fetchLatestComicNum(cls):
        '''
        Update the latest comic number in the website and store in class attribute
        '''
        try:
            mainPage = requests.get('http://www.lefthandedtoons.com/', headers = headers)
            mainPage.raise_for_status()
        except Exception as exc:
            raise Exception('Error connecting with lefthandedtoons');                               logging.error(f'{str(exc) = }')

        mainPageSoup = bs4.BeautifulSoup(mainPage.text, 'lxml')
        try:
            latestComicLink = mainPageSoup.select(
                '#comicwrap > div.comicnav.top > div > h1 > a')[0].get('href')
            latestComicNum = int(os.path.basename(latestComicLink.rstrip('/')))
        except Exception as exc:
            raise Exception('Unable to fetch latest comic. Please check if the website changed'); logging.error(f'{str(exc) = }')

        # update class attribute
        cls.latestComicNum = latestComicNum


directory = '/mnt/0FBF0B0B0FBF0B0B/betaCode/update'
downloader = LeftHandedToons()
downloader.downloadComics(directory)
