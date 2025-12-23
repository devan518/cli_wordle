from colorama import *
import requests

'''
for i in guess: 
    if i == word[0:-1:1] 
        if i == for j in word: 
            correct(i) 
        else: 
            correct_wrong()
logic:
'''

print("WARNING! Program may pick a hard word based of the api design. Sorry!")
while True:
    config_one = input("how much letters should your wordle be? (minimum is 3)")
    length = int(config_one)
    if length < 3:
        print("Enter Valid Number!")
    else:
        break
    
init(autoreset=True) #colorama start coloring!

def main():
    url = "https://random-word-api.herokuapp.com/word"
    params = {"length": length}
    response = requests.get(url, params=params, timeout=5,)
    response.raise_for_status()

    word = response.json()[0]
    print(word) #for debug
    answer = list(word)
    
    for count in range(6): #attempts left
        for i in range(length): #iterate thru each character
            line = []
            guess = list(input())
        
            if len(guess) != len(answer):
                print("ERROR! THE INPUTTED GUESS IS NOT THE SAME LENGTH AS ANSWER")

            if guess[i] == answer[i]:
                line.append("green")
                print(Style.BRIGHT + Back.GREEN + Fore.WHITE + " " + guess[i] + " ",end="")
                break
            elif guess[i] in answer:
                line.append("yellow")
                print(Style.BRIGHT + Back.YELLOW + Fore.WHITE + " " + guess[i] + " ",end="")
                break
            elif guess[i] not in answer:
                line.append("grey")
                print(Style.BRIGHT + Back.LIGHTBLACK_EX + Fore.WHITE + " " + guess[i] + " ",end="")
                break
            elif line[0:-1] == "green":
                print("YOU WIN!")
                return

    print("you lost! the answer was " + answer +"!")

if __name__ == "__main__":
    main()