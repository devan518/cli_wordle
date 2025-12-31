from colorama import *
import requests
from google import genai

#init ai client for generating word and also hint
client = genai.Client(api_key="AIzaSyDxSUHNpAOb5VjoVB0KThspuu1c7d2t9SE")
#to make sure that ai doesnt show the same words over and over
words = []

def check(guess: str, answer: str, length: int):
    line = []
    for i in range(length): #iterate thru each character
        if guess[i] == answer[i]:
            line.append("green")
        elif guess[i] in answer: 
            line.append("yellow")
        elif guess[i] not in answer:
            line.append("grey")
    for i in range(len(line)):
        if line[i] == "green":
            print(Style.BRIGHT + Fore.WHITE + Back.GREEN + " " + guess[i] + " ", end="") #green
        elif line[i] == "yellow":
            print(Style.BRIGHT + Fore.WHITE + Back.YELLOW + " " + guess[i] + " ", end="") #yellow
        elif line[i] == "grey":
            print(Style.BRIGHT + Fore.WHITE + Back.LIGHTBLACK_EX + " " + guess[i] + " ", end="") #yello
    res = set(line)
    if res == "green":
        return True
    else:
        return False
def pick_word(length):
    prompt = f'You are WordleBot. Your job is to create words to be fit in a wordle game. Here are your instructions: Generate a word (respond with only that one word): that is {length} letters long, is not one of these words: {words}, and respond in lowercase.'
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    return response.text
def hint(word):
    prompt = f'You are HintBot. Respond with a short, one sentence hint that doesnt give it away, but just gives the player an idea of what the word is, for guessing a word in a wordle game. Your word is {word}'
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    return response.text

def main():
    banner = '''
 ██████╗ ██╗     ██╗
██╔════╝ ██║     ██║
██║      ██║     ██║
██║      ██║     ██║
╚██████╗ ███████╗██║
 ╚═════╝ ╚══════╝╚═╝

██╗    ██╗ ██████╗ ██████╗ ██████╗ ██╗     ███████╗
██║    ██║██╔═══██╗██╔══██╗██╔══██╗██║     ██╔════╝
██║ █╗ ██║██║   ██║██████╔╝██║  ██║██║     █████╗  
██║███╗██║██║   ██║██╔══██╗██║  ██║██║     ██╔══╝  
╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝███████╗███████╗
 ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝

Hello! This is my  version of wordle, written as a cli!
features:
-generates word using ai instead of pre picked words so that is doesnt run out!

-use "/hint" as a command to get a hint!

-custom wordle length!
'''
    print(banner)
    while True:
        config_one = input("how much letters should your wordle be? (minimum is 3)")
        length = int(config_one)
        if length < 3:
            print("Enter Valid Number!")
            continue
        else:
            break
    
    init(autoreset=True) #colorama start coloring!
    word = pick_word(length)
    for count in range(6): #attempts left
        guess = input()

        if guess == "/hint":
            print(hint(word))

        if len(guess) != len(word):
            print("ERROR! THE INPUTTED GUESS IS NOT THE SAME LENGTH AS ANSWER")
        
        if check(guess, word, length) == True:
            print("\n You Won!")
            choice = input("Would you like to try again? (yes/no)")
            if choice == "yes":
                main()
            else:
                return
        else:
            pass
    print("\n You Lost!😔")
    choice = input("Would you like to try again? (yes/no)")
    if choice == "yes":
        main()
    else:
        return
    
if __name__ == "__main__":
    main()