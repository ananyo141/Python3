# Search for questions in StackOverflow
import tkinter.filedialog, sys, os, logging
from ModuleImporter import module_importer
requests = module_importer('requests', 'requests')
bs4 = module_importer('bs4', 'beautifulsoup4')

logging.basicConfig(level = logging.INFO, format = '%(asctime)s - %(levelname)s - %(lineno)d - %(message)s')
logging.disable(logging.CRITICAL)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
}

def main(): 
    if len(sys.argv) < 2:
        sys.exit("Usage: python <script.py> <tags>")
    try:
        numPages = int(input("How many StackOverflow pages you want to scrape for answers?: "))
    except:
        sys.exit("Expected Integer Input")

    downloadDir = tkinter.filedialog.askdirectory()
    if not downloadDir:
        sys.exit("No download directory chosen")
    logging.info(f'{downloadDir = }')

    tags = ('-').join(sys.argv[1:])

    for pageNum in range(1, numPages + 1):
        file = open(downloadDir + os.sep + 'Page ' + str(pageNum) + '.txt', mode = 'w');    logging.info(f'Starting Page {pageNum}')
        print('\n' + f'Scraping Page: {pageNum} of {numPages}'.center(50))
    
        mainPageLink = 'https://stackoverflow.com/questions/tagged/' + tags + '?tab=votes&page=' + str(pageNum) + '&pagesize=15'
        logging.warning(f'{mainPageLink = }')
        try:
            mainPage = requests.get(mainPageLink, headers = headers)
            mainPage.raise_for_status()
        except Exception as exc:
            sys.exit("Unable to reach StackOverflow at the moment\n\n" + str(exc))
        
        mainPageSoup = bs4.BeautifulSoup(mainPage.text, 'lxml');                        logging.debug(f'{mainPageSoup = }')
        # Write the introduction
        introduction = mainPageSoup.select('div.mb24>p')[0].getText();                  logging.info(f'{introduction = }')
        file.write(introduction + '\n\n')
        file.write(f'Page Number: {pageNum}'.center(100) + '\n')
        questionLinks = mainPageSoup.select('div.summary a.question-hyperlink');        logging.info(f'{questionLinks = }')
        print(f"Found {len(questionLinks)} questions".center(50) + '\n')
        for questionTag in questionLinks:
            questionUrl = 'https://www.stackoverflow.com' + questionTag.get('href');    logging.info(f'{questionUrl = }')
            question = questionTag.getText().strip();                                   logging.info(f'{question = }')
            # Get into the question page
            try:
                questionPage = requests.get(questionUrl, headers = headers)
                questionPage.raise_for_status();                                        logging.info(f'{questionPage.status_code = }')
            except Exception as exc:
                print(f"Unable to fetch question: {question} from {questionUrl}.\n" + str(exc))
                print("Continuing...")
                continue

            questionPageSoup = bs4.BeautifulSoup(questionPage.text, 'lxml');            logging.debug(f'{questionPageSoup = }')
            fullQuestion = questionPageSoup.select('#question > div.post-layout > div.postcell.post-layout--right > div.s-prose.js-post-body')[0].getText().strip()
            answers = questionPageSoup.select('div.answercell.post-layout--right div.s-prose.js-post-body');        logging.debug(f'{answers = }'); logging.info(f'{len(answers) = }'); logging.info(f'{fullQuestion = }')
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
    print(f"\nSuccessfully scraped StackOverflow for questions tagged: '{tags}' and saved results in {downloadDir}") 

if __name__ == '__main__':
    main()
