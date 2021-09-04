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


import tkinter.filedialog, threading, requests, bs4, logging, sys, os
from ModuleImporter import module_importer

logging.basicConfig(level = logging.INFO, format = "%(asctime)s - %(levelname)s - %(lineno)d - %(message)s",
                    datefmt = "%d/%m/%Y %I:%M:%S %p", filename = "updateWebsites.log", filemode = "w")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
}

# create classes and methods for each website

class LeftHandedToons:
    latestComicNum = 0

    def __init__(self):
        self.comicDownloaded = 0

    # Download comics 
    def downloadComic(self, downloadDir, **kwargs):
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
                try:
                    page = requests.get(f"http://www.lefthandedtoons.com/{pageNum}/", headers = headers)
                    page.raise_for_status()
                except Exception as exc:
                    print(f"Unable to download comic #{pageNum}");                       logging.error(f"{pageNum = }\n{str(exc)}")
                    continue
                pageSoup = bs4.BeautifulSoup(page.text, 'lxml')
                try:
                    imgLink = pageSoup.select('#comicwrap > div.comicdata > img')[0].get('src')
                except IndexError:
                    print(f"Unable to find image for comic #{pageNum}");                       logging.error(f"{pageNum = }")
                    continue
                
                # download image
                try:
                    image = requests.get(imgLink, headers = headers)
                    image.raise_for_status()
                except Exception as exc:
                    print(f"Error saving comic #{pageNum}");                       logging.error(f"{pageNum = }\n{str(exc)}")
                    continue

                imageFileName = os.path.join(saveDir, os.path.basename(imgLink))
                with open(imageFileName, 'wb') as imageFile:
                    for chunk in image.iter_content(1000000):
                        imageFile.write(chunk)


        # Initialize start and stop
        startComic = kwargs.get('startComic', 1)   # comic range starts from 1
        stopComic  = kwargs.get('endComic', LeftHandedToons.latestComicNum + 1)  # since stop is non-inclusive

        comicPerThread = 10
        for start in range(startComic, stopComic, comicPerThread):
            stop = start + comicPerThread
            if stop > stopComic:
                stop = stopComic


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


# LeftHandedToons.updateLatestComicNum()
print(LeftHandedToons.latestComicNum)
