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
    


init(autoreset=True) #colorama start coloring!!!

def correct(letter):
    print(Style.BRIGHT + Back.GREEN + Fore.WHITE + " " + letter + " ",end="")

def correct_wrong(letter):
    print(Style.BRIGHT + Back.YELLOW + Fore.WHITE + " " + letter + " ",end="")

def wrong(letter):
    print(Style.BRIGHT + Back.LIGHTBLACK_EX + Fore.WHITE + " " + letter + " ",end="")

def main():
    url = "https://random-word-api.herokuapp.com/word"
    params = {"length": length}
    response = requests.get(url, params=params, timeout=5,)
    response.raise_for_status()

    word = response.json()[0]

    answer = list(word)
    for count in range(length):
        guess = input("\n type in your guess: ")
        if len(guess) == length:
            pass
        else:
            print("ERROR: GUESS CANNOT BE MORE THAN" + str(length) + "LETTERS!")
            continue
    
        for i in answer:
            if guess[i] == answer[i]:
                correct(i)
            else:
                if guess in answer:
                    correct_wrong(i)
                else:
                    wrong()
        
            

    print("you lost! the answer was " + answer +"! Wanna play again? type 'yes' to restart!")
    restart = input()
    if restart == "yes":
        return True
    else:
        print("ERROR")
if __name__ == "__main__":
    main()
    
                




    
    





