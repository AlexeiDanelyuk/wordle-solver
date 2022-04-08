# wordle-solver
## How to run it

1. Download and install python
2. Install selenium: `pip install selenium`
3. Install RegEx: `pip install regex`
4. Install Chrome WebDriver from: [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)
5. Install termcolor: `pip install termcolor`
6. Run like you would normally in a command line: `python wordle.py`

## How it works

So far, it is borderline bruteforcing.

### Interacting with the page

It takes in the link of the official NYT Wordle game and goes to the page. It uses **selenium** to execute JavaScript code on the website to close the popup, press the keyboard buttons, and get the status of each letter once a word has been entered (absent, present, or correct).

### The Logic

As I said, this is borderline bruteforce. For the first three attempts, it will try the words *AEROS*, *UNTIL*, and *PYGMY*. These words have been worked out with a different script of mine (word-analyzer.py) as being three best consecutive words for eliminating the majority of the possible words. 

After each word is entered, their status (absent, present, correct) is noted and a RegEx is constructed to rid the list of all the words that it could not possibly be.

After the three words have been entered, the script makes a guess at which word it could be by taking the first word on the now shortened list of possible words. Continue until successful.