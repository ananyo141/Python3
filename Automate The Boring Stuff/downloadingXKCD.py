# Downloading XKCD Comics

import requests, bs4, tkinter.filedialog, sys, os
import logging
# filename = './log.txt'
logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(lineno)d - %(message)s')
logging.disable(logging.CRITICAL)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
}

def main():
    print("Choose where you want to archive XKCD")
    downloadDir = tkinter.filedialog.askdirectory()
    if not downloadDir:
        sys.exit("No directory chosen")

    logging.info(f'{downloadDir = }')
    previousPageLink = ''
    count = 1
    while previousPageLink != '#':

        logging.info(f'{previousPageLink = }')
        # download the main page   
        mainPageLink = 'https://www.xkcd.com' + previousPageLink
        try:
            mainPage = requests.get(mainPageLink, headers = headers)
            mainPage.raise_for_status()
            logging.info(f'{mainPage.status_code = }')
        except Exception as exc:
            print("Unable to connect to xkcd.com\nException: " + str(exc))
            sys.exit()

        mainPageSoup = bs4.BeautifulSoup(mainPage.text, 'lxml')
        imageTag = mainPageSoup.select('#comic img')
        previousPageLink = mainPageSoup.find('a', rel='prev').get('href')

        if imageTag == []:
            print(f"No comic found at {mainPageLink}")
            continue
        # download image
        imageName = imageTag[0].get('alt')[:240].replace('/','') + '.png'
        imageUrl = 'https://' + imageTag[0].get('src').lstrip('/')

        logging.debug(f'{imageName}')
        try:
            image = requests.get(imageUrl, headers = headers)
            image.raise_for_status()
        except Exception as exc:
            print("Unknown error occurred\n" + str(exc) + '\nContinuing...')
            continue

        print(f"Searching page {mainPageLink}")
        print(f"Saving comic {count} ID-{previousPageLink.replace('/', '')}: {imageName}...\n")
        count += 1
        try:
            file = open(downloadDir + os.sep + imageName, mode = 'wb')
        except Exception as exc:
            print('Unknown error occurred\n' + str(exc) + f'\n{imageName} not saved' + '\nContinuing...')
            continue
        for chunk in image.iter_content(1000000):
            file.write(chunk)
        file.close()


if __name__ == '__main__':
    main()