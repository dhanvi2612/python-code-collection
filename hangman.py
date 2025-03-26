#HANGMAN
import random
import requests

letters_guessed = [] #initialising all variables
word_shown = []
vowels=["a","e","i","o","u"]
hangmen={1:"\n\n\n",2:"  O\n\n",3:"  O\n  |\n",4:"  O\n/ |\n",5:"  O\n/ | \\\n",6:"  O\n/ | \\ \n /",7:"  O\n/ | \\ \n / \\"}
guessno = 1

def getwords(): #getting a list of all words in the english dictionary using requests and api
        allwords=requests.get("https://www.randomlists.com/data/words.json").json()
        words=allwords["data"]
        return words


def starting(): #selecting word and initialising
    global word_chosen,word_shown
    word_chosen = list(random.choice(getwords()))
    word_shown=["_" if letter not in vowels else letter for letter in word_chosen ]


def play(guessesno):
    global word_chosen, word_shown, letters_guessed, win
    while True:
        print(f"\n\nGuess {guessesno}/{7}") #displaying guesses done
        print(f"--------\n{hangmen[guessesno]}\n--------") #displaying the man
        print("Word: "," ".join(word_shown).upper())
        while True: #validating guess
            user = input("Enter your letter guess: ").lower()
            if user in vowels:
                print("You guessed a vowel.")
            elif not user.isalpha() or len(user) != 1:
                print("Invalid guess.")
            elif user in letters_guessed:
                print("You've already guessed that letter.")
            else:
                letters_guessed.append(user)
                break


        i = 0
        var=False
        for b in word_chosen: #updating the display
            if user==b:
                word_shown[i]=user
                var=True
            i=i+1
        if var==True: #printing to the user
            print("That's in the word!")
        else:
            print("That's not in the word!")
            guessesno += 1

        if guessesno==7: #end game conditions
            print(f'\n\n\nYou ran out of guesses.\n{hangmen[7]}\n')
            print(f'*********YOU LOSE!*********')
            win=None
            break
        elif word_chosen==word_shown:
            print(f"\n\n\nYou guessed all the letters!\n")
            print('*********YOU WIN!*********')
            break

def main(): #initialising the game
    starting()
    play(guessno)
    print("\n\nThe word was"," ".join(word_chosen).upper())

if __name__ == "__main__":
    main()