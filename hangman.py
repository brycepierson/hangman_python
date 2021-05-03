import random
import re

class hangmanGameState:
    def __init__(self, maxWrongGuesses=6):
        self.guessedLetters = []
        self.maxWrongGuesses = maxWrongGuesses
        self.numWrongGuesses = 0
    def initializeGameState(self):
        self.__init__()
class hangman:
    def __init__(self):
        self.wordList = list(map(str.strip, open("words.txt").readlines()))
        self.gameState = hangmanGameState()
        random.seed()
        
    def start(self):
        while(1):
            self.gameState.initializeGameState()
            print("Welcome to Hangman: The Game!")
            randomWord = self.chooseRandomWord()
            self.mainGameLoop(randomWord)
            print("Play again?")
            answer = input(":").lower()
            if answer == "y" or answer == "yes":
                pass
            else:
                break
        
        print("GOODBYE!")

    def chooseRandomWord(self):
        return self.wordList[random.randrange(len(self.wordList))].lower()

    def replaceLetter(self, letter, magicWord, guessingWord):
        indices = [m.start() for m in re.finditer(letter, magicWord)]
        for index in indices:
            i = int(index)
            if i is not 0:
                guessingWord = guessingWord[:i*2] + letter + guessingWord[i*2 + 1:]
            else:
                guessingWord = letter + guessingWord[1:]
        return guessingWord

    def askForGuess(self, guessingWord):
        while(1):
            print("*************************")
            print(guessingWord)
            print()
            print("Guessed Letters: [" + ", ".join(self.gameState.guessedLetters) + "]")
            print("Guesses Remaining: " + str(self.gameState.maxWrongGuesses - self.gameState.numWrongGuesses))
            print("*************************")
            guess = input(":")
            if len(guess) >= 1 and guess.isalpha():
                if guess in self.gameState.guessedLetters:
                    print("ERROR! Try guessing a new letter!")
                else:
                    return guess
            else:
                print("ERROR! PLEASE GUESS A LETTER OR A WORD!\n")

    def mainGameLoop(self, magicWord):
        guessed = False
        outOfGuesses = False
        guessingWord = '_ ' * len(magicWord)
        while(not guessed and not self.outOfGuesses()):
            guess = self.askForGuess(guessingWord)
            if len(guess) == 1 and guess not in self.gameState.guessedLetters and guess not in magicWord:
                self.gameState.guessedLetters.append(guess)
            if guess not in magicWord:
                self.gameState.numWrongGuesses += 1
            if guess in magicWord:
                guessingWord = self.replaceLetter(guess, magicWord, guessingWord)
            if '_' not in guessingWord:
                guessed = True
                break
        if guessed:
            print("CONGRATULATIONS! You won!")
        else:
            print("Too Bad! Out of guesses! The word was: " + magicWord)



    def outOfGuesses(self):
        return self.gameState.numWrongGuesses >= self.gameState.maxWrongGuesses


if __name__ == "__main__":
    myHangman = hangman()
    myHangman.start()