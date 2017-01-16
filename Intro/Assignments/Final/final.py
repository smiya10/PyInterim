"""
This program does several basic calculations and conversions in the shell
See the Readme (which may or may not exist for this example project) for more details
"""

welcome = """Welcome to SciTool.
You can convert units by using the command "convert [num] [unit] to [unit]"
You can do simple math by using the command "calc [num] [operator] [num]"
See the documentation for a complete list of details"""

request = ">>> "

def init():
    """
    Prints the welcome message and may do some other random init stuff
    """
    print(welcome)

def loop():
    """
    Does the loop stuff for each iteration of the SciTool
    :return: Returns True if the user wants to quit
    """
    command = input(request).split(" ")
    if len(command) >= 1:
        if command[0] == "quit":
            return True
        elif command[0] == "calc":
            if len(command) == 4:
                answer = calc(float(command[1]), command[2], float(command[3]))
                if answer == False:
                    print("Operator unavailable")
                else:
                    print(answer)
            else:
                print("Invalid calc syntax")
        elif command[0] == "convert":
            if len(command) == 5 and command[3] == "to":
                answer = convert(float(command[1]), command[2], command[4])
                if answer == False:
                    print("Conversion unavailable")
                else:
                    print(answer)
            else:
                print("Invalid convert syntax")
        else:
            print("Invalid command")
    return False

length_units = {"km":1000, "m":1, "cm":0.1, "mm":0.001, "in":0.0254, "ft": 0.3048, "yd":0.9144, "mi":1609.34}
mass_units = {"kg":1, "g":0.001, "mg":0.000001, "lb":0.453592, "oz":0.0283495}
units = (length_units, mass_units)
    
def convert(num, from_unit, to_unit):
    """
    Converts between units
    :param num: Initial number float
    :param from_unit: Initial unit string
    :param to_unit: Unit to which to convert
    :return: Returns the number in new units, False if unable to convert
    """
    
    for unit_dict in units:
        if from_unit in unit_dict:
            if to_unit in unit_dict:
                return num * unit_dict[from_unit] / unit_dict[to_unit]
    return False
    
def calc(num1, op, num2):
    """
    Does a simple 2-number calculation (as in 2 + 2)
    :param num1: First number in calculation
    :param op: Operator
    :param num2: Second number in calculation
    :return: Returns the value of the evaluated calculation, False if unable to calc
    """
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2
    elif op == "^":
        return num1 ** num2
    else:
        return False

if __name__ == "__main__":
    init()
    done = False
    while not done:
        done = loop()

