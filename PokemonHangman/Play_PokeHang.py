# Reads in Pokemon list from text file
import random
Pokefile = open("PokemonList.txt",'r')
Pokemon = Pokefile.readlines()
Pokefile.close()
# Sets game play loop
playing = "YES"
while playing == "YES":
    # initializes Pokemon name to be guessed with question marks equalling letters 
    Pokeword = random.choice(Pokemon)
    Pokeword = Pokeword.strip().upper()
    Mystery_word = ""
    for let in Pokeword:
        Mystery_word = Mystery_word + "?"
    # Intializes count of guesses and guessed letters
    GuessNum = 7
    print("\n" + Mystery_word)
    GuessList = []
    # Sets loop until game won or lost
    while GuessNum != 0 and Mystery_word.isalpha() == False:
        # Lets user guess a letter and ensures it is one letter and has not been guessed before
        oneLet = False
        while oneLet == False:
            GuessLetter = str(input("Enter a letter ")).upper()
            if GuessLetter in GuessList:
                print("Letter already guessed. Please choose another letter.")
            elif len(GuessLetter) == 1 and GuessLetter.isalpha() == True:
                oneLet = True
            else:
                print("Error. Enter one letter please.")
        GuessList.append(GuessLetter)
        # Checks and notifies if a letter is in the Pokemon name and subtracts from guess count if incorrect
        PokeIndex = 0
        letCount = 0
        for let in Pokeword:
            if let == GuessLetter:
                Mystery_word = Mystery_word[:PokeIndex] + GuessLetter + Mystery_word[PokeIndex + 1:]
                letCount = letCount + 1
            PokeIndex = PokeIndex + 1
        if letCount == 0:
            GuessNum = GuessNum - 1
            print(f"The letter {GuessLetter} is not correct. Number of guesses left is {GuessNum}")
        else:
            print(f"The letter {GuessLetter} is correct. Number of guesses left is {GuessNum}")
        print("\n" + "Guessed letters are " + str(GuessList))
        print(Mystery_word + "\n")
    # Notifies if game won or lost
    if GuessNum == 0:
        print(f"Sorry, you lost this game. The pokemon was {Pokeword}")
    else:
        print(f"You win. {Pokeword} was the right answer")
    # Asks to keep play or game
    playing = input("Play again (YES/NO)? ").upper()
    if playing != "YES" and playing != "NO":
        playing = input("Please enter YES or NO? ").upper()