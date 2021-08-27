# Create multithreaded selenium that plays 2048.
import tkinter.filedialog, concurrent.futures, sys, random, time
from ModuleImporter import module_importer
selenium = module_importer('selenium', 'selenium')

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def play2048(gecko_path: str) -> int:
    '''Creates an instance of Firefox and plays a game of 2048 and returns the score'''

    moves = [Keys.UP, Keys.DOWN, Keys.LEFT, Keys.RIGHT]
    browser = webdriver.Firefox(executable_path = gecko_path)
    browser.get('https://play2048.co/')
    htmlElem = browser.find_element_by_tag_name('html')
    while True:
        htmlElem.send_keys(random.choice(moves))
        try:
            browser.find_element_by_css_selector('.game-message.game-over')
            break
        except:
            continue
    
    # find and convert the current score
    currentScore = browser.find_element_by_css_selector('div.score-container').text
    currScoreIndex = currentScore.rfind('\n')
    if currScoreIndex != -1:
        currentScore = currentScore[:currScoreIndex]

    time.sleep(3)   # wait for the user to see results
    browser.quit()
    try:
        return int(currentScore)                                                                # try return score by converting str->int,
    except ValueError:                                                                          # if website changes and cannot convert score,
        raise Exception("Error getting the current score! Cannot convert " + currentScore)      # throw exception to update function   
                                                                                                

def main():
    print("Enter the firefox gecko driver:")
    gecko = tkinter.filedialog.askopenfilename()
    if not gecko:
        sys.exit("Gecko driver not selected")
    try:
        numGames = int(input('How many games you want to watch through?: '))
    except ValueError:
        sys.exit("Expected integer input")

    # Create separate thread for each game
    with concurrent.futures.ThreadPoolExecutor() as executor:
        threads = [executor.submit(play2048, gecko) for i in range(numGames)]

    # collect the score that each thread returns
    scores = [thread.result() for thread in threads]

    # print the result
    print("\n" + " Thank you for playing 2048 ".center(50, '*'))
    print(f"Games Played: {numGames} ")
    print(f"Best Score: {max(scores)}")
    print(f"Lowest Score: {min(scores)}")
    print(f"Average Score: {round(sum(scores)/numGames, 2)}\n")


if __name__ == '__main__':
    main()
