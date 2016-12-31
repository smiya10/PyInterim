# We need a run loop, as this is a continous, user ended program
# If we get to functions fast enough, make it polish!
while(True):
    user_input = (input("$ ")).strip()
    
    # Give the user an opton to quit the program. Kinda essential.
    if (user_input == "quit"):
        break
        
    # We assume that the user enters valid input
    # Split by whitespace
    user_input = user_input.split()
    
    # Now find what operator they entered
    operator = user_input[1]

    # Now get the operands
    try:
        right = float(user_input[0])
        left = float(user_input[2])
    except:
        print("Please enter only numbers and one operator. This calculator can only do one thing at a time!")
        continue
    
    # Now to determine what exactly they want to do
    if operator == "+":
        print(str(right + left))
    elif operator == "-":
        print(str(right - left))
    elif operator == "*":
        print(str(right * left))
    elif operator == "/":
        print(str(right / left))
    elif operator == "%":
        print(str(right % left))
    elif operator == "**":
        print(str(right ** left))
    else:
        print("Operator not found. Please try again")
        
print("Bye!")
# I'm happy with this.
