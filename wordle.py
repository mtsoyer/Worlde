from random import randrange


class WD:
    
    def __init__(self, main_word, count):
        self.main_word = main_word
        self.count = count
        self.flag = True
    
    def main(self, guess):
        while (self.count < 7 and self.flag):
            print(f"Your word is {guess}. You have { 7- self.count} try(ies) left!")
            
            if (len(guess) != 5):
                if (guess == "QUIT"):
                    print("Thanks for playing!")
                    return False
                elif (guess == "HINT"):
                    print(f"The middle letter of your word is {self.main_word[2]} \n")
                    self.try_again()
                    
                print(f"Your word isn't long enough, or it's too long! Try again! You have {7 - self.count} try(ies) left!")
                self.try_again()

            print(self.checkWord(self.main_word.rstrip(), guess.rstrip()))
            
            if (self.main_word.rstrip() == guess.rstrip()):
                self.won(self.main_word)
                print("Thanks for playing!")
                self.flag = False
                return
                
                
            else:
                self.try_again()
        print("You lose!")       
    
    def checkWord(self, main_word, guess):
        characters = {
                0: "no",
                1: "no",
                2: "no",
                3: "no",
                4: "no",
                
            }
        
        for n in range(len(guess)):
                if guess[n] == main_word[n]:
                    characters[n] = "yes"
                elif guess[n] in main_word:
                    characters[n] = "maybe"

        results = ""
            
        for n in range(len(guess)):
            if (characters[n] == "yes"):
                results += " ^" + guess[n]
            elif (characters[n] == "maybe"):
                results += " *" + guess[n]
            else:
                results += "   " + guess[n]
        return results
    
    def won(self, main_word):
        self.flag = False
        print(f"You got the word right! It was {main_word}!")
        
    def try_again(self):
        print("Try again!")
        word = input("Type here! << ").upper()
        self.count += 1
        self.main(word)      
                
    def generateWord():
        file = "C:/Users/Motheo/Documents/Python/wordle/words.txt"
        word_array = []
        with open(file) as file_object:
            for line in file_object:
                word_array.append(line)
        num = randrange(len(word_array))
        return word_array[num]
    
    
print("Welcome to Wordle! Guess a five letter word! If a * appears next to a letter, it means that letter is" +
                  "in the word. If you get a ^ above the letter, it means that letter is in that exact same position in the word. If you get nothing, then.. well, it's nothing! \n")
print(f"If you want to quit, type QUIT. If you want a hint, type HINT! \n")
    
guess = input("Enter your word here: << " ).upper()


print(f"Your word is {guess}")
    
ob = WD(WD.generateWord().upper(), 1)
ob.main(guess)
        
        
