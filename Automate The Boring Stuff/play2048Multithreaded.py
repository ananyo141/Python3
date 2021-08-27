# Create multithreaded selenium that plays 2048.
# Use selenium to play the 2048 game
import tkinter.filedialog, threading, sys, random, time
from ModuleImporter import module_importer
selenium = module_importer('selenium', 'selenium')

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Global Variable to keep track of scores
scores = []

def play2048(gecko_path: str) -> None:
    '''Creates an instance of Firefox and plays a game of 2048 and saves the score in global 'scores' list'''

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

    # wait for the user to see results
    time.sleep(5)
    browser.quit()
    try:
        global scores
        scores.append(int(currentScore))                                                        # try to save score into global variable (from str->int),
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

    threads = []
    for i in range(numGames):
        playThread = threading.Thread(target = play2048, args = [gecko])
        playThread.start()
        threads.append(playThread)

    for thread in threads:
        thread.join()

    print("Thank you for playing 2048")
    print("Games Played: ", numGames,", Best Score: ", max(scores),
          ", Average Score: ", sum(scores)/numGames, sep='')


if __name__ == '__main__':
    main()
