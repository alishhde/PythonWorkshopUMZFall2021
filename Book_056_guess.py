from random import randint

computer_guess = randint(1, 10)
user_guess = 11
while computer_guess != user_guess:
    user_guess = int(input("Enter a number: "))
else: print(f"Nice guess you both choose {computer_guess}")