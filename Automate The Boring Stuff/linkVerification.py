# Verify the links in a given webpage.
import sys
from ModuleImporter import module_importer
requests = module_importer('requests', 'requests')
bs4 = module_importer('bs4', 'beautifulsoup4')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
}

def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: Enter the website url in command line\n")
    websiteUrl = 'http://' + sys.argv[1]
    try:
        webpage = requests.get(websiteUrl, headers = headers)
    except Exception as exc:
        sys.exit("The website is unreachable\n" + str(exc))
    
    if webpage.status_code == 404:
        print("Page not found (404) for " + websiteUrl)
        
    webpageSoup = bs4.BeautifulSoup(webpage.text, 'lxml')
    links = webpageSoup.select('a')
    nonWorkingLink = False
    for linkTag in links:
        linkUrl = linkTag.get('href')
        if not linkUrl:
            continue

        if linkUrl.find('https://') == -1:
            linkUrl = websiteUrl + linkUrl
        print("Validating link: " + linkUrl)
        try:
            linkPage = requests.get(linkUrl, headers = headers)
        except:
            continue

        if linkPage.status_code == 404:
            print(f"Found non-working link: {linkUrl} {str(linkPage.status_code)}")
            nonWorkingLink = True

    if not nonWorkingLink:
        print("No Links were broken on " + websiteUrl)   



if __name__ == '__main__':
    main()
