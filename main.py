from colorama import *
import requests

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
def pick_letter(length):
    url = "https://random-word-api.herokuapp.com/word"
    params = {"length": length}
    response = requests.get(url, params=params, timeout=5,)
    response.raise_for_status()
    word = response.json()[0]
    return word
def main():
    print("\nWARNING! Program may pick a hard word based of the api design. Sorry!")
    while True:
        config_one = input("how much letters should your wordle be? (minimum is 3)")
        length = int(config_one)
        if length < 3:
            print("Enter Valid Number!")
            continue
        else:
            break
    
    init(autoreset=True) #colorama start coloring!
    word = pick_letter(length)
    for count in range(6): #attempts left
        guess = input()
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