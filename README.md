# CS450 Wordle Wizards

### Authors: Jackson McCoy, Paul Nusser, Nate Webb, Katherine Nemits

## Introduction:

This repository contains a set of Python scripts designed to manage and enhance the Wordle game experience. Wordle is a word-guessing game where players attempt to guess a secret word within a limited number of attempts.

The scripts provide functionalities for playing the Wordle game, implementing an AI solver for assistance, managing game state and logic, and generating visualizations of game statistics.

## AI Assistance:

If the user chooses to enable the AI, it will provide recommendations for the best next guesses based on the potential entropy of the words. These calculations are made to potentially increase the amount of information gained from a “good” guess, enabling the AI to further narrow down the potential answer words.

## Running the Game:

To play the Wordle game, execute: *python WordleGame.py*

You will then be prompted to choose whether or not to enable the Wordle Solver AI. If you enable it, the top potentially best guesses will be provided and you will be prompted to make your first guess. This will continue until you guess the correct secret word or until you use all 6 guesses.

To exit the game at any time type: *exit*.

### Results

Results of a guess will come in this form: *[('t', 2), ('a', 1), ('r', 0), ('e', 1), ('s', 2)]*

These results break up every letter and assign it a 0, 1, or 2. 
- 0 means the letter is grey and not present anywhere in the secret word.
- 1 means the letter is yellow and is present in the word but not in that position.
- 2 means the letter is correct and in the correct position.

At the end of the game, the user is prompted on whether or not they would like to view a plot of the letter distribution in guesses. If multiple games were run it also outputs a histogram of the number of guesses it took each round.

### autoEnable

Within the wordleGame, the variable *autoEnable* is set to False. If set to True the game will run automatically, choosing the top suggested guess each time. The graphs will be created at the end.

## Dependencies

This project is built using Python programming language and relies on the matplotlib library for visualization.

- matplotlib is used to generate optional histograms to illustrate the average number of guesses and the letter usage distribution for testing purposes.

## Contents:

- wordleGame.py - Manages the Wordle game, including initializing game instances, filling word lists, setting hidden words, and playing the game.
- wordleSolver.py - Provides a Wordle solver class that assists in solving the game by calculating potential entropies and pruning the list of possible guesses to narrow down possible answers.
- gameState.py - Manages the state and logic of the Wordle game, including updating guesses, checking words, and initializing game state.
- valid_guesses.txt - Contains a list of valid guess words.
- valid_solutions.txt - Contains a list of all valid word solutions.
- wordsAndEntropies.txt - Contains a list of up to 10 of the best guesses with the highest potential entropy.

## Class Documentations:

### wordleGame.py

**Class: game**

Constructors:
- game: Initializes a game instance with a gameState object.

Methods:
- fillWordLists: Fills the validGuesses and validSolutions lists from external files.
- setToList: Converts set of words to list of valid words.
- setHiddenWord: Randomly selects a secret word from validSolutions list.
- displayGraphs: Plots a graph of Letter frequencies in guesses and a graph of average number of guesses.

### wordleSolver.py

**Class: patternMatrix**

Constructors:
- patternMatrix:  Initializes the pattern matrix and prones it to remove invalid combinations.

Methods:
- calculateHashValue: Calculates the has value of a given pattern.
- pruneMatrix: Removes combinations where the sum of the first 5 elements is 9.

**Class: wordleSolver**

Constructors:
- wordleSolver: Initializes the Wordle solver AI.

Methods:
- calculateExpectedEntropy: Calculates the potential entropy of a given word based on probabilities.
- countOccurances: Counts the number of times a letter appears in word lists.
- calculateTopNExpectedEntropies: Calculates the top N expected entropies of words.
- updateWordLists: Updates the Wordle solver's word lists based on the guessed word and its letters corresponding color information.
- deleteGreyWords: Removes any words containing grey letters.
- deleteGreyDupes: Deletes words containing duplicate grey letters from the Wordle solver's word lists.
- keepYellowWords: Removes all words with yellow letter in guessed position.
- keepGreenWords: Removes words where green letters are not in guessed positions

### gameState.py

**Class: gameState**

Constructors:
- gameState: Initializes the game state with default values.

Methods:
- updateGuesses: Updates list of guesses with latest guess and feedback.
- checkWord2: Checks if guessed word is secret word and generates feedback.
- checkWord: checks for matched indices and then for partial matches.

## Sources
https://www.youtube.com/watch?v=v68zYyaEmEA
https://medium.com/codex/building-a-wordle-solver-with-python-77e3c2388d63
