# mathQuiz.py
# Grant Andrews
# 4/14/22
# This program gives simple math quizes to a user with random numbers each time.
# The program asks the user to enter their answer and provides feedback as to 
# whether the user was correct or not.

# Here, the random module in being imported.
import random

# This is the main function that contains all other functions and specifies the
# order in which they should run.
def main():
   while True:
      num1, num2 = choose_random()
      answer = showProblem(num1, num2)
      user_response = getAnswer()
      showCorrect(answer, user_response)
      play_again = keep_going()
      
      if play_again == 'n':
         print("Goodbye!")
         break

#This function randomly assigns a number to both num1 and num2 variables and 
# returns them to the main function.
def choose_random():
   num1 = random.randint(0,1000)
   num2 = random.randint(0,1000)
   return num1, num2

# This function prints the math problem to the user and also calculates what the
# correct answer is. The answer is returned to the main function.
def showProblem(num1, num2):
   print(num1, "+", num2)
   answer = num1 + num2
   return answer

#This function asks the user to enter their answer and returns the user answer to
# the main function. Error checking is implemented to ensure that the user only
# enters a numerical value and not a string.
def getAnswer():
   
   print("Please enter the sum:")
   while True:
      try:
         user_response = float(input())
         break
      except ValueError:
         print("Please enter a number only!")
   
   return user_response

# This function prints to the user the results of their answer, either correct
# or incorrect. 
def showCorrect(answer, user_response):
   if answer == user_response:
      print("Your are correct! The answer is", answer)
   else:
      print("Incorrect! The answer is", answer)

# This function asks the user if they would like to play again. The response
# is returned to the main function where the response is evaluated. 
def keep_going():
   
   play_again = input("Would you like to try again? Please enter 'Y' or 'N'\n").lower()
   
   while play_again != 'y' and play_again != 'n':
      play_again = input("Please enter 'Y' or 'N'\n").lower()
      
   return play_again
  
# Here, the main function is being called which will allow the code to run.    
main()

