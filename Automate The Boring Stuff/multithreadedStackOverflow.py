# Search for questions in StackOverflow
import tkinter.filedialog, threading, time, sys, os, logging
from ModuleImporter import module_importer
requests = module_importer('requests', 'requests')
bs4 = module_importer('bs4', 'beautifulsoup4')

logging.basicConfig(filename = 'multithreadedStackOverflow.log', level = logging.ERROR, format = "%(asctime)s - %(levelname)s - %(lineno)d - %(message)s",
                    datefmt = '%d/%m/%Y - %I:%M:%S %p', filemode = 'w')
# logging.disable(logging.CRITICAL)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
}

# keep track of 429 Too Many Requests Client Errors
clientErr = 0

def downloadStackOverflow(pageNum, numPages, tags, downloadDir):
    file = open(downloadDir + os.sep + 'Page ' + str(pageNum) + '.txt', mode = 'w');    logging.info(f'Starting Page {pageNum}')

    mainPageLink = 'https://stackoverflow.com/questions/tagged/' + tags + '?tab=votes&page=' + str(pageNum) + '&pagesize=15'
    logging.warning(f'{mainPageLink = }')
    try:
        mainPage = requests.get(mainPageLink, headers = headers)
        mainPage.raise_for_status()
    except Exception as exc:
        sys.exit("Unable to reach StackOverflow at the moment\n\n" + str(exc));     logging.error(f'{str(exc) = }')
    
    mainPageSoup = bs4.BeautifulSoup(mainPage.text, 'lxml');                        logging.debug(f'{mainPageSoup = }')
    # Write the introduction
    introduction = mainPageSoup.select('div.mb24>p')[0].getText();                  logging.info(f'{introduction = }')
    file.write(introduction + '\n\n')
    file.write(f'Page Number: {pageNum}'.center(100) + '\n')
    questionLinks = mainPageSoup.select('div.summary a.question-hyperlink');        logging.info(f'{questionLinks = }')
    for index, questionTag in enumerate(questionLinks):
        if index >= 10:        # write maximum 10 questions (due to StackOverflow request restrictions)
            break
        questionUrl = 'https://www.stackoverflow.com' + questionTag.get('href');    logging.info(f'{questionUrl = }')
        question = questionTag.getText().strip();                                   logging.info(f'{question = }')
        # Get into the question page
        try:
            questionPage = requests.get(questionUrl, headers = headers)
            questionPage.raise_for_status();                                        logging.info(f'{questionPage.status_code = }')
        except Exception as exc:
            if str(exc).startswith('429'):
                global clientErr
                clientErr += 1
                if clientErr > 7:
                    print('Server Timeout')
                    return
                else:
                    continue
            print(f"Unable to fetch question: {question} from {questionUrl}.\n" + str(exc))
            print("Continuing...");                                                 logging.error(f'{str(exc) = }')
            continue

        questionPageSoup = bs4.BeautifulSoup(questionPage.text, 'lxml');            logging.debug(f'{questionPageSoup = }')
        fullQuestion = questionPageSoup.select('#question > div.post-layout > div.postcell.post-layout--right > div.s-prose.js-post-body')[0].getText().strip()
        answers = questionPageSoup.select('div.answercell.post-layout--right div.s-prose.js-post-body');        logging.debug(f'{answers = }'); logging.info(f'{len(answers) = }'); logging.info(f'{fullQuestion = }')

        print(f'Scraping Page: {pageNum} of {numPages}')
        print(f"Searching question: {question[:240]}...")
        print(f'Found {len(answers)} answers')

        file.write('\n\n' + ' Question: '.center(100,'*'))
        file.write('\n\n' + question)
        file.write(fullQuestion + '\n\n')
        file.write(f"Answers found: {len(answers)}".rjust(100) + '\n')
        # write the answers
        for i in range(len(answers)):
            file.write('\n\n' + f' Answer {i + 1} '.center(100, '-') + '\n\n')
            file.write(answers[i].getText())

    file.close()

def main(): 
    if len(sys.argv) < 2:
        sys.exit("Usage: python <script.py> <tags>")

    numPages = 20       # for safe scraping, so that stack overflow doesn't block IP address

    downloadDir = tkinter.filedialog.askdirectory()
    if not downloadDir:
        sys.exit("No download directory chosen")
    logging.info(f'{downloadDir = }')

    tags = ('-').join(sys.argv[1:])
    start_time = time.time()
    threads = []
    for pageNum in range(1, numPages + 1):
        downloadThread = threading.Thread(target = downloadStackOverflow, args = [pageNum, numPages, tags, downloadDir])
        # allow 10 threads at a time
        if len(threads) % 10 == 0:
            for thread in threads:
                thread.join()
            threads = []
        threads.append(downloadThread)
        downloadThread.start()

    # join the remaining threads
    for remainingThread in threads:
        remainingThread.join()
    end_time = time.time()
    print(f"\nSuccessfully scraped StackOverflow for questions tagged: '{tags}' and saved results in {downloadDir}") 
    print("Total Time taken: %.2f seconds" % (end_time - start_time))


if __name__ == '__main__':
    main()
