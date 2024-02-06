import random


class GuessingGame:
    
 
    def __init__(self, answer):
        self.answer = answer
        self.solved_it = False
        
   
    def guess(self, user_guess):
        self.user_guess = user_guess
        message = ""
        if self.user_guess < self.answer:
            message += 'low'
        elif self.user_guess > self.answer:
            message += 'high'
        elif self.user_guess == self.answer:
            message += 'Correct'
            self.solved_it = True
        return message
        
        
    def solved(self):
        return self.solved_it
    
game = GuessingGame(random.randint(1,100))
last_guess  = None
last_result = None

while game.solved() == False:
  if last_guess != None: 
    print(f"Oops! Your last guess ({last_guess}) was {last_result}.")
    print("")

  last_guess  = int(input("Enter your guess: "))
  last_result = game.guess(last_guess)


print(f"{last_guess} was correct!")      
        


# game = GuessingGame(10)

# print(game.solved())   # => False

# game.guess(5)  # => 'low'
# game.guess(20) # => 'high'
# print(game.solved())   # => False

# game.guess(10) # => 'correct'
# print(game.solved())   # => True

"""
# I need user input  
# generat random number
# set a limit to the number of guess
# I need a loop to check the guesses
    
    """