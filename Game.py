import random

class Game:
    def __init__(self):
        self.wordList = []
        self.filePath = ""
        self.secretWord = ""
        self.wordFound = False
        self.attempts = 0
        self.userGuess = ""
        self.wordList = []
    
    def fillwordList(self):
        newWordList = []
        self.wordList = newWordList

    def setToList(wordSet):
        return list(wordSet)
    
    def setHiddenWord(wordList):
        random_index = random.randint(0, (wordList.length()) - 1)
        return wordList[random_index]
    
    def checkWord(guess,self):
        numList = []
        found = False
        for i in range(5):
            for j in range(5):
                if (self.secretWord[j] == guess[i]):
                    if (j == i):
                        numList.append[2]
                        found = True
                        break
                    else:
                        numList.append[1]
                        found = True
                        break
            if (found == False):
                numList.append[0]
        return numList


    
    def playGame(self):
        self.filePath = input("enter the filePath of the list of all words: ")
        wordSet = Game.fillSet(self.filePath)
        self.wordList = Game.setToList(wordSet)
        self.secretWord = Game.setHiddenWord(self.wordList)
        valGuess = False

        while (self.wordFound == False & self.attempts < 6) :
            while (valGuess == False) :
                self.userGuess = input("make a guess: ") 
                if (len(self.userGuess) == 5):
                    valGuess = True
            
            



            
        

class gamestate:

    def __init__(self) -> None:
        self.guesses = []


    
    def updateGuesses(self, word):
        self.guesses.append(word)
