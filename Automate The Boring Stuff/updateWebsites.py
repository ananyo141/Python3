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


import tkinter.filedialog, threading, logging, pprint, time, sys, os
from ModuleImporter import module_importer

requests = module_importer('requests', 'requests')
bs4 = module_importer('bs4', 'beautifulsoup4')

logging.basicConfig(level = logging.INFO, format = "%(asctime)s - %(levelname)s - %(lineno)d - %(message)s",
                    datefmt = "%d/%m/%Y %I:%M:%S %p", filename = "updateWebsites.log", filemode = "w")

# create classes and methods for each website
class LeftHandedToons:
    latestComicNum = None
    # User-Agent to make script requests emulate an actual browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }

    def __init__(self, downloadDir):
        self.comicDownloaded = 0
        self.saveDir = os.path.join(downloadDir, 'LeftHandedToons')
        # initialize once during creation of first object instance
        if LeftHandedToons.latestComicNum == None:
            LeftHandedToons.fetchLatestComicNum()

    def downloadImage(self, imageUrl):
        ''' Download the given imageUrl in the object directory '''

        try:
            image = requests.get(imageUrl, headers = LeftHandedToons.headers)
            image.raise_for_status()
        except Exception as exc:
            print(f"Error saving comic {imageUrl}");                                     logging.error(f"{imageUrl = }\n{pprint.pformat(str(exc))}")
            return

        imageFileName = os.path.join(self.saveDir, os.path.basename(imageUrl));                logging.debug(f"{imageFileName = }")
        with open(imageFileName, 'wb') as imageFile:
            for chunk in image.iter_content(1000000):
                imageFile.write(chunk)

        self.comicDownloaded += 1


    # nested target function
    def downloadComicSq(self, start, stop):
        ''' Download comics sequentially, this is going to be the target function for threading '''

        os.makedirs(self.saveDir, exist_ok = True)
        for pageNum, imgLink in LeftHandedToons.getLatestComicLinks(start, stop):
            
            print("Downloading Comic #%-4d: %s..." % (pageNum, os.path.basename(imgLink)))
            # download image
            self.downloadImage(imgLink)

    # Download comics 
    def downloadComics(self, **kwargs):
        '''Download comic to the given downloadDir according to given arguments
        with threading support

        Support optional keyword arguments:
        startComic = (1 by default), 
        endComic = (latestComicNum + 1 by default)
        '''

        # Initialize start and stop
        startComic = kwargs.get('startComic', 1)   # comic range starts from 1
        stopComic  = kwargs.get('endComic', LeftHandedToons.latestComicNum + 1)  # since stop is non-inclusive

        comicPerThread = 10
        start_time = time.time()
        threads = []    # thread buffer
        for start in range(startComic, stopComic, comicPerThread):
            stop = start + comicPerThread
            if stop > stopComic:
                stop = stopComic

            logging.debug(f'{start = }, {stop = }')
            downloadThread = threading.Thread(target = self.downloadComicSq, args = [start, stop])
            threads.append(downloadThread)
            downloadThread.start()

        # wait for downloads
        for thread in threads:
            thread.join()
        end_time = time.time()
        print("Download finished in %.2f seconds" % (end_time - start_time))

    def updateDirectory(self):
        ''' Update the object directory for any new comics by going reverse order from the latest comic '''

        updated = False

        # for i in range(LeftHandedToons.latestComicNum, 1, -1):
        #     pageLink = 



    @classmethod
    def fetchLatestComicNum(cls):
        ''' Update the latest comic number in the website and store in 'latestComicNum' class attribute '''

        try:
            mainPage = requests.get('http://www.lefthandedtoons.com/', headers = LeftHandedToons.headers)
            mainPage.raise_for_status()
        except Exception as exc:
            raise Exception('Error connecting with lefthandedtoons');                             logging.error(f'{str(exc) = }')

        mainPageSoup = bs4.BeautifulSoup(mainPage.text, 'lxml')
        try:
            latestComicLink = mainPageSoup.select(
                '#comicwrap > div.comicnav.top > div > h1 > a')[0].get('href')
            latestComicNum = int(os.path.basename(latestComicLink.rstrip('/')))
        except Exception as exc:
            raise Exception('Unable to fetch latest comic. Please check if the website changed'); logging.error(f'{str(exc) = }')

        # update class attribute
        cls.latestComicNum = latestComicNum

    @classmethod
    def getLatestComicLinks(cls, start, stop):
        for pageNum in range(start, stop):
            pageLink = f"http://www.lefthandedtoons.com/{pageNum}/"
            try:
                page = requests.get(pageLink, headers = LeftHandedToons.headers)
                page.raise_for_status()
            except Exception as exc:
                print(f"Unable to download comic #{pageNum}");                               logging.error(f"{pageLink = }\n{pprint.pformat(str(exc))}")
                continue
            pageSoup = bs4.BeautifulSoup(page.text, 'lxml')
            try:
                imgLink = pageSoup.select('#comicwrap > div.comicdata > img')[0].get('src')
            except IndexError as exc:
                print(f"Unable to find image for comic #{pageNum}");                         logging.error(f"{imgLink = }, {pageNum = }\n{pprint.pformat(str(exc))}")
                continue

            yield pageNum, imgLink



def main():
    directory = tkinter.filedialog.askdirectory()
    if not directory:
        sys.exit("No directory chosen")
    directory = os.path.normpath(directory)     # make path windows-like in windows

    LHTDownloader = LeftHandedToons(directory)
    LHTDownloader.downloadComics()


if __name__ == '__main__':
    main()
