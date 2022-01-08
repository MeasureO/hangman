import random
import string

class Hangman:
    def __init__(self):
        print("H A N G M A N")
        self.game()
    
    def __str__(self):
        return "H A N G M A N"
    
    def play(self):
        words = ('python', 'java', 'kotlin', 'javascript')
        word = random.choice(words)
        board = ["-"] * len(word)
        tries = 8
        memory = set()
        while tries > 0:
            print()
            print(*board, sep="")
            letter = input("Input a letter: ")
            if len(letter) > 1:
                print("You should input a single letter") 
                continue
            if letter not in string.ascii_lowercase:
                print("Please enter a lowercase English letter")
                continue  
            if letter in memory:
                    print("You've already guessed this letter")
                    #tries -= 1
                    continue
            elif letter in word:
                for i in range(len(word)):
                    if word[i] == letter:
                        board[i] = letter
            else:
                print("That letter doesn't appear in the word")
                tries -= 1
            memory.add(letter)
            if "".join(board) == word:
                print(*board, sep="")
                print("You guessed the word!")
                print("You survived!")
                break
        else:
            print("You lost!")
        
    def game(self):
        while True:
            command = input('Type "play" to play the game, "exit" to quit: ')
            if command == 'play':
                self.play()
                break
            elif command == 'quit':
                break
            else:
                continue
            
    
game_session = Hangman()
        
    
