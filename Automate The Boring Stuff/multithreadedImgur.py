#!python3
# This program takes user input from command line and downloads images into user selected folder

import threading, sys, os, tkinter.filedialog, time, logging
from ModuleImporter import module_importer
requests = module_importer('requests', 'requests')
bs4 = module_importer('bs4', 'beautifulsoup4')
slugify = module_importer('slugify', 'python-slugify')

logging.basicConfig(filename = 'multhreadedImgur.log', level = logging.INFO, format = "%(asctime)s - %(levelname)s - %(lineno)d - %(message)s",
                    datefmt = '%d/%m/%Y - %I:%M:%S %p', filemode = 'w')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
}

def downloadImgur(mainPageSoup, i, imagesLinks, downloadDir):
    imageName = mainPageSoup.select('div.hover>p')[i].getText().replace('/', ' ')[:100];    logging.warning(f'{imageName = }')
    imageUrl = imagesLinks[i].get('href');                                                  logging.info(f'{imageUrl = }')
    imageCode = imageUrl[imageUrl.rfind('/'):];                                             logging.warning(f'{imageCode = }')

    print(f"Downloading Image {i + 1}: {imageName[:50]}...")
    try:
        downloadImage = requests.get('https://i.imgur.com' + imageCode + '.jpg', headers = headers)
        downloadImage.raise_for_status()
    except Exception as exc:
        print("\nUnexpected error:\n" + str(exc))
        return


        
    # writing the downloaded file
    fileName = downloadDir + os.sep + slugify.slugify(imageName) + '.jpg';                  logging.critical(f'{fileName = }')
    # for duplicate image names
    count = 1
    fileStem = os.path.splitext(fileName)[0];                                               logging.critical(f'{fileStem = }')
    while os.path.exists(fileName):
        fileName = fileStem + str(count) + '.jpg'
        count += 1

    with open(fileName, mode = 'wb') as file:
        for chunk in downloadImage.iter_content(1000000):
            file.write(chunk)
    # time.sleep(0.4)         # To avoid blocking of script requests

def main():
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
        sys.exit("No directory chosen.");                                           logging.debug(f'{downloadDir = }')
    downloadDir = os.path.normpath(downloadDir)

    url = 'https://imgur.com/r/' + keywords;                                        logging.info(f'{url = }')

    try:
        mainPage = requests.get(url, headers = headers);                            logging.warning(f'{mainPage.status_code = }')
        mainPage.raise_for_status()
    except Exception as exc:
        print("\nUnable to connect to Imgur.")
        sys.exit('Check your internet connection and try again.\n\n' + str(exc))

    mainPageSoup = bs4.BeautifulSoup(mainPage.text, 'lxml');                        logging.debug(f'{mainPageSoup = }')
    
    # get the list of the image tags
    imagesLinks = mainPageSoup.select('a.image-list-link');                         logging.debug(f'{imagesLinks = }')
    if len(imagesLinks) == 0:
        sys.exit("No images found on Imgur")

    threads = []
    start_time = time.time()
    for i in range(min(len(imagesLinks), numImages)):
       downloadThread = threading.Thread(target = downloadImgur, args = [mainPageSoup, i, imagesLinks, downloadDir])
       threads.append(downloadThread)
       downloadThread.start()

    # wait for threads to complete
    for thread in threads:
        thread.join()

    end_time = time.time()
    print("Download Completed, time taken = %.2f seconds" % (end_time - start_time))
    print(f"Files saved at directory: {downloadDir}")


if __name__ == '__main__':
    main()
