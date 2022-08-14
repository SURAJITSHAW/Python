secret_number = 13
guess_start = 0
guess_limit = 3

# In python else statment can be associated with while loop.
while guess_start < guess_limit:
    guess = int(input("Guess: "))
    guess_start += 1
    if guess == secret_number:
        print("You win!")
        break
# this else part will only run if condition for while loop returns false.
else: 
    print("You failed!!!")