#guessNumber.py
import random

key=random.randint(1, 10)   
x=int(input("Guess The Number Between 1 to 10: "))
if x==key:
    print("congratulations, you have guessed the right Number")
else:
    print("you have guessed wrong number")