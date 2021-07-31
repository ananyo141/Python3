#!python3
# This program searches Amazon website for the product entered by the user

import webbrowser, requests, bs4, sys

# So that Amazon doesn't block script requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
}

def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: <script>.py {product to search}")
    keyword = (' ').join(sys.argv[1:])

    try:
        numResults = int(input("How many products do you want to list?: "))
    except:
        sys.exit("Invalid. Expected integer input")

    tries = 0
    # To bypass 'not found' bug
    while True:
        try:
            searchPage = requests.get('https://www.amazon.in/s?k=' + keyword + '&ref=nb_sb_noss', headers = headers)
            searchPage.raise_for_status()
        except:
            sys.exit("Unable to connect to Amazon. Try again later.")

        formattedPage = bs4.BeautifulSoup(searchPage.text, 'html.parser')    
        # Remove duplicate product links
        linkElems = list(set(formattedPage.select('a.a-link-normal.a-text-normal')))
        if len(linkElems) == 0:                         # if no products found
            if tries > 5:
                sys.exit("No products found. Try using different keywords.")

            tries += 1
            continue
        else:
            break

    numOpen = min(numResults, len(linkElems))       # If a products are fewer than number entered
    # print the names of the found products
    for i in range(numOpen):
        print(f'Product {i + 1}:', linkElems[i].getText())
    if input("Do you want to view these products in your browser?(Y/N): ").lower().startswith('y'):
        print("Opening in browser")
        # open the links for each of the products
        for i in range(numOpen):
            webbrowser.open('amazon.in' + linkElems[i].get('href'))
    else:
        print("Aborted")

if __name__ == '__main__':
    main()