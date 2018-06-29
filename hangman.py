from random import *

def hangman():
	print("LET'S PLAY HANGMAN!!!")

	say = input("How many words do you want our Word Bank to have? ")
	lengthBank = int(say);
	wordBank = []
	for i in range(0,lengthBank):
		word = input("Type a word for someone to guess: ")
		word = word.lower()
		if(word.isalpha() == False):
			print("That's not a word!")
		wordBank.append(word)
	word = wordBank[randint(0,lengthBank-1)]
	wordList = list(word)
	length = len(word)
	guessList = ["_"]*length
	#print(wordList)
	print(guessList)
	lettersGuessed = []
	tries=6
	print("Guesses: ")
	print(lettersGuessed)
	print("Tries: ")
	print(tries)

	while (tries>0):
		guess = input("Guess a letter: ")
		if(guess in wordList):
			for i in range(len(wordList)):
				if (wordList[i] == guess):
					guessList[i] = guess
			if("_" not in guessList):
				print("You did it, congrats! The word is " + word)
				break
			print(guessList)
		if(guess not in wordList):
			lettersGuessed.append(guess)
			tries-=1
			print(guessList)
			print(lettersGuessed)
			print("Tries: " + str(tries))
	if(tries==0):
		print("You lose! The word was: " + word)

