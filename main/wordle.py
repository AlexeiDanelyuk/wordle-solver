from selenium import webdriver
import time
import re
from termcolor import colored

driver = webdriver.Chrome()

driver.get("https://www.nytimes.com/games/wordle/index.html")
driver.maximize_window()
time.sleep(2)

def reset_page():
    driver.delete_all_cookies()
    driver.refresh()
    driver.execute_script('document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-modal").shadowRoot.querySelector("div > div > div").click();')
    time.sleep(1)    

def click_A ():
    driver.execute_script('document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(2) > button:nth-child(2)").click();')

def click_B ():
    driver.execute_script('document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(3) > button:nth-child(6)").click();')

def click_C ():
    driver.execute_script('document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(3) > button:nth-child(4)").click();')

def click_D ():
    driver.execute_script('document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(2) > button:nth-child(4)").click();')

def click_E ():
    driver.execute_script('document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(1) > button:nth-child(3)").click();')
    
def click_F ():
    driver.execute_script('document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(2) > button:nth-child(5)").click();')

def click_G ():
    driver.execute_script('document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(2) > button:nth-child(6)").click();')

def click_H ():
    driver.execute_script('document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(2) > button:nth-child(7)").click();')

def click_I ():
    driver.execute_script('document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(1) > button:nth-child(8)").click();')

def click_J ():
    driver.execute_script('document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(2) > button:nth-child(8)").click();')

def click_K ():
    driver.execute_script('document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(2) > button:nth-child(9)").click();')

def click_L ():
    driver.execute_script('document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(2) > button:nth-child(10)").click();')

def click_M ():
    driver.execute_script('document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(3) > button:nth-child(8)").click();')

def click_N ():
    driver.execute_script('document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(3) > button:nth-child(7)").click();')

def click_O ():
    driver.execute_script('document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(1) > button:nth-child(9)").click();')

def click_P ():
    driver.execute_script('document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(1) > button:nth-child(10)").click();')

def click_Q ():
    driver.execute_script('document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(1) > button:nth-child(1)").click();')

def click_R ():
    driver.execute_script('document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(1) > button:nth-child(4)").click();')

def click_S ():
    driver.execute_script('document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(2) > button:nth-child(3)").click();')

def click_T ():
    driver.execute_script('document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(1) > button:nth-child(5)").click();')

def click_U ():
    driver.execute_script('document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(1) > button:nth-child(7)").click();')

def click_V ():
    driver.execute_script('document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(3) > button:nth-child(5)").click();')

def click_W ():
    driver.execute_script('document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(1) > button:nth-child(2)").click();')

def click_X ():
    driver.execute_script('document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(3) > button:nth-child(3)").click();')

def click_Y ():
    driver.execute_script('document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(1) > button:nth-child(6)").click();')

def click_Z ():
    driver.execute_script('document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(3) > button:nth-child(2)").click();')

def click_ENTER ():
    driver.execute_script('document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(3) > button:nth-child(1)").click();')

# here for testing purposes
def click_BACKSPACE ():
    driver.execute_script('document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(3) > button:nth-child(9)").click();')

keyboard = { "ENTER" : click_ENTER,
            "BACKSPACE" : click_BACKSPACE,
            "A" : click_A,
            "B" : click_B,
            "C" : click_C,
            "D" : click_D,
            "E" : click_E,
            "F" : click_F,
            "G" : click_G,
            "H" : click_H,
            "I" : click_I,
            "J" : click_J,
            "K" : click_K,
            "L" : click_L,
            "M" : click_M,
            "N" : click_N,
            "O" : click_O,
            "P" : click_P,
            "Q" : click_Q,
            "R" : click_R,
            "S" : click_S,
            "T" : click_T,
            "U" : click_U,
            "V" : click_V,
            "W" : click_W,
            "X" : click_X,
            "Y" : click_Y,
            "Z" : click_Z
}

# get all possible wordle words 
# file obtained from "https://gist.github.com/dracos/dd0668f281e685bad51479e5acaadb93"
r = open('valid-wordle-words.txt', 'r')

words = []
for line in r:
    if line != "\n":
        words.append(line.strip())
r.close()

duration = 0.1

#word = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#blacklisted letters 
blacklist_letters = ["","","","",""]

#greenlisted letters
greenlist_letters = ["","","","",""]

#yellowlisted letters
yellowlist_letters = ["","","","",""]
yellowlist_stack = []

regex = ""
regex_letters=["","","","",""]

iteration = 0

solved = False

# FIRST RUN
input_word = "AEROS"

# begin search
while solved != True:
    reset_page()
    for i in range(6):
        iteration += 1
        print(colored("Iteration #" + str(iteration) + " - Trying word: " + input_word.upper(), 'magenta'))

        for letter in input_word:
            time.sleep(duration)
            keyboard[letter.capitalize()]()
        keyboard["ENTER"]()

        time.sleep(3)

        for j in range(5):
            time.sleep(duration)
            status = driver.execute_script('return document.querySelector("body > game-app").shadowRoot.querySelector("#board > game-row:nth-child('+str(i+1)+')").shadowRoot.querySelector("div > game-tile:nth-child('+str(j+1)+')").getAttribute("evaluation");')
            words_to_remove = []
            if status == "absent":
                blacklist_letters[j] = input_word[j].lower()
            elif status == "present":
                yellowlist_letters[j] = input_word[j].lower()
                if input_word[j].lower() not in yellowlist_stack:
                    yellowlist_stack.append(input_word[j].lower())
            elif status == "correct":
                greenlist_letters[j] = input_word[j].lower()
                if input_word[j].lower() in yellowlist_stack:
                    yellowlist_stack.remove(input_word[j].lower())

        print(colored("Result of try: ", 'blue'), end='')
        for letter in range(5):
            if input_word[letter].lower() == blacklist_letters[letter]:
                print(colored(str(input_word[letter]).upper(), 'white'), end='')
            elif input_word[letter].lower() == yellowlist_letters[letter]:
                print(colored(str(input_word[letter]).upper(), 'yellow'), end='')
            elif input_word[letter].lower() == greenlist_letters[letter]:
                print(colored(str(input_word[letter]).upper(), 'green'), end='')
        print("")

        word_found = True
        for letter in greenlist_letters:
            if letter == "":
                word_found = False
                solved = True


        if word_found:
            print(colored("Word found!", 'cyan'))
            break

        for letter in range(5):
            if greenlist_letters[letter] == "" and yellowlist_letters[letter] == "":
                regex_letters[letter] += "[^"
                for b_letter in blacklist_letters:
                    if b_letter in yellowlist_stack:
                        if letter == blacklist_letters.index(b_letter):
                            regex_letters[blacklist_letters.index(b_letter)] += b_letter
                        continue
                    regex_letters[letter] += b_letter
                regex_letters[letter] += "]"
            elif greenlist_letters[letter] != "" and yellowlist_letters[letter] == "":
                regex_letters[letter] += greenlist_letters[letter]
            elif greenlist_letters[letter] == "" and yellowlist_letters[letter] != "":
                regex_letters[letter] += "[^"
                for b_letter in blacklist_letters:
                    regex_letters[letter] += b_letter
                regex_letters[letter] += yellowlist_letters[letter]
                regex_letters[letter] += "]"
                    

        blacklist_letters = ["","","","",""]
        yellowlist_letters = ["","","","",""]

        regex_string = ""
        for ex in regex_letters:
            regex_string += ex

        regex_letters = ["","","","",""]

        r = re.compile(regex_string)

        words = list(filter(r.match, words))

        for word in words:
            for letter in yellowlist_stack:
                if letter not in word:
                    words_to_remove.append(word)

        words_to_remove = list(dict.fromkeys(words_to_remove))

        for word in words_to_remove:
            words.remove(word)

        words_to_remove.clear()

        print(colored("Remaining words: " + str(words), 'magenta'))
        
        if i == 0:
            input_word = "UNTIL"
        elif i == 1:
            input_word = "PYGMY"
        else:
            input_word = words[0]

print(colored("Remaining words: " + str(words), 'magenta'))