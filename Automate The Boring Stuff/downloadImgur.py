#!python3
# This program takes user input from command line and downloads images into user selected folder

import requests, bs4, sys, os, tkinter.filedialog, time
import logging

# filename = './log.txt'
logging.basicConfig(level = logging.DEBUG, format = ' %(asctime)s - %(levelname)s - %(lineno)d - %(message)s')
logging.disable(logging.CRITICAL)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
}

def main():
    logging.info('Starting program')
    if len(sys.argv) < 2:
        sys.exit("Usage: <script>.py {keywords}")

    keywords = ('+').join(sys.argv[1:])
    try:
        numImages = int(input("How many images do you want to download?: "))
    except ValueError:
        sys.exit("Invalid response. Expected integer input")
    
    # Take the download directory
    downloadDir = tkinter.filedialog.askdirectory()
    if not downloadDir:
        sys.exit("No directory chosen.")
    logging.debug(f'{downloadDir = }')

    url = 'https://imgur.com/r/' + keywords
    logging.info(f'{url = }')

    tries = 0
    while True:
        try:
            mainPage = requests.get(url, headers = headers)
            logging.warning(f'{mainPage.status_code = }')
            mainPage.raise_for_status()
            if mainPage.status_code == requests.codes.ok:
                break
        except Exception as exc:
            print("\nUnable to connect to Imgur.")
            if tries > 5:
                sys.exit('Check your internet connection and try again.\n\n' + str(exc))
            print(f"Retrying...({tries})")
            tries += 1
            time.sleep(1)
            continue

    tries = 0
    mainPageSoup = bs4.BeautifulSoup(mainPage.text, 'lxml')
    logging.debug(f'{mainPageSoup = }')
    
    # get the list of the image tags
    imagesLinks = mainPageSoup.select('a.image-list-link')
    logging.debug(f'{imagesLinks = }')
    if len(imagesLinks) == 0:
        sys.exit("No images found on Imgur")

    for i in range(min(len(imagesLinks), numImages)):
       
        imageName = mainPageSoup.select('div.hover>p')[i].getText().replace('/', ' ')[:240]
        imageUrl = imagesLinks[i].get('href')
        imageCode = imageUrl[imageUrl.rfind('/'):]

        logging.info(f"{imagesLinks[i].get('href')}")
        logging.info(f'{imageUrl = }')
        logging.warning(f'{imageName = }')
        logging.warning(f'{imageCode = }')
        print(f"Downloading Image {i + 1}: {imageName[:50]}...")
        try:
            downloadImage = requests.get('https://i.imgur.com' + imageCode + '.jpg', headers = headers)
            downloadImage.raise_for_status()
        except Exception as exc:
            print("\nUnexpected error:\n" + str(exc))
            if tries > 5:
                sys.exit()
            print(f"Retrying...({tries})")
            tries += 1
            continue

        tries = 0
        # writing the downloaded file
        fileName = downloadDir + os.sep + imageName + '.jpg'
        # for duplicate image names
        count = 1
        fileStem = os.path.splitext(fileName)[0]
        while os.path.exists(fileName):
            fileName = fileStem + str(count) + '.jpg'
            count += 1

        logging.critical(f'{fileName = }')
        file = open(fileName, mode = 'wb')
        for chunk in downloadImage.iter_content(1000000):
            file.write(chunk)
        file.close()
        # time.sleep(0.4)         # To avoid blocking of script requests

    print("Download Completed")
    print(f"Files saved at directory: {downloadDir}")


if __name__ == '__main__':
    main()