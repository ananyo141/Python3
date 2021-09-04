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
        pass

    # Download comics 
    def downloadComic(self, downloadDir, **kwargs):
        '''Download comic to the given downloadDir according to given arguments
        Support optional keyword arguments:
        startComic = (1 by default) 
        endComic = (latestComicNum by default)
        '''

        # Initialize start and stop
        start = kwargs.get('start', 1)   # comic range starts from 1
        stop = kwargs.get('stop', LeftHandedToons.latestComicNum + 1)  # since stop is non-inclusive


    @classmethod
    def updateLatestComicNum(cls):
        '''
        Find the latest comic number in the website
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


LeftHandedToons.updateLatestComicNum()
print(LeftHandedToons.latestComicNum)
