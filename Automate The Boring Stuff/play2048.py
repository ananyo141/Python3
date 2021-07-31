# Use selenium to play the 2048 game
import tkinter.filedialog, sys, random, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def main():
    moves = [Keys.UP, Keys.DOWN, Keys.LEFT, Keys.RIGHT]
    print("Enter the firefox gecko driver:")
    gecko = tkinter.filedialog.askopenfilename()
    if not gecko:
        sys.exit("Gecko driver not selected")
    try:
        numGames = int(input('How many games you want to watch through?: '))
    except ValueError:
        sys.exit("Expected integer input")

    browser = webdriver.Firefox(executable_path = gecko)
    totalScore = 0
    for i in range(numGames):
        browser.get('https://play2048.co/')
        htmlElem = browser.find_element_by_tag_name('html')
        while True:
            htmlElem.send_keys(random.choice(moves))
            try:
                browser.find_element_by_css_selector('.game-message.game-over')
                break
            except:
                continue
        
        currentScore = browser.find_element_by_css_selector('div.score-container').text
        currScoreIndex = currentScore.rfind('\n')
        if currScoreIndex != -1:
            currentScore = currentScore[:currScoreIndex]

        print("Game " + str(i + 1) + " Score: " + currentScore)
        totalScore += int(currentScore)
        time.sleep(3)

    bestScore = browser.find_element_by_css_selector('div.best-container').text
    browser.quit()
    print("Thank you for playing 2048")
    print("Last Game Score: ", currentScore,
          ", Best Score: ", bestScore,
          ", Average Score: ", totalScore/numGames, sep='')


if __name__ == '__main__':
    main()