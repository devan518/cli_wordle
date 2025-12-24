from colorama import *
import requests

print("WARNING! Program may pick a hard word based of the api design. Sorry!")
while True:
    config_one = input("how much letters should your wordle be? (minimum is 3)")
    length = int(config_one)
    if length < 3:
        print("Enter Valid Number!")
    else:
        break
    
init(autoreset=True) #colorama start coloring!

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

def main():
    url = "https://random-word-api.herokuapp.com/word"
    params = {"length": length}
    response = requests.get(url, params=params, timeout=5,)
    response.raise_for_status()

    word = response.json()[0]
    #print(word) #for debug
    
    for count in range(6): #attempts left
        guess = input()
        if len(guess) != len(word):
            print("ERROR! THE INPUTTED GUESS IS NOT THE SAME LENGTH AS ANSWER")
        check(guess, word, length)
        print("")

if __name__ == "__main__":
    main()