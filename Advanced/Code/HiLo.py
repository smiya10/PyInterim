import random

user_max = input("Max Number: ")
rand = random.randint(0, user_max)
count = 0
max_allowed = math.ceil(math.log(user_max)) 

while count < max_allowed:
    user_input = input("Guess a number: ")
    if user_input == rand:
        print("You win!")
        break
    elif user_input < rand:
        print("Too Low!")
    else:
        print("Too High!")
    count += 1
    
if count == max_allowed:
    print("Game Over. Too Bad :(")
print("Attempts: " + count)
