# Machine Learning for Dummies, John Paul Mueller, Luca Massaron
# Use: open a terminal and run python, then import the file using "import mlfordum" or "from mlfordum import *".
# If you use "import mlfordum", you would need to type "mlfordum." followed by the function you want to use.

# sending required arguments
def DoSum(value1, value2):
    return value1+value2

# sending arguments by keywords
def DisplaySum(value1, value2):
    print(str(value1) + " + " + str(value2) + " = " + str((value1+value2)))

# DisplaySum(1,2)
# DisplaySum(2,3)
# DisplaySum(value2=3, value1=2)

# giving function arguments a default value
def SayHello(greetings="No Value Supplied"):
    print(greetings)

# SayHello()
# SayHello("Howdy!")

# creating functions with a variable number of arguments
def DisplayMulti(argcount = 0, *varargs):
    print('You passed ' + str(argcount) + ' arguments. ', varargs)

# working with global and local variables
mystr = "Hello"

def printStr():
    global mystr
    print(mystr)
    mystr = "There!"
    print(mystr)

# making decisions using the if statement
def testValue(value):
    if value == 5:
        print('Value equals 5!')
    elif value == 6:
        print('Value equals 5!')
    else:
        print('Value is something else.')
        print('It equals ' + str(value))

# choosing between multiple options using nested decisions
def secretNumber():
    one = int(input(("Type a number between 1 and 10: ")))
    two = int(input(("Type a number between 1 and 10: ")))

    if one >= 1 and one <= 10:
        if two >= 1 and two <= 10:
            print('Your secret number is: ' + str(one * two))
        else:
            print("Incorrect second value!")
    else:
        print("Incorrect first value!")

# performing repetitive tasks using for
def displayMulti(*varargs):
    for arg in varargs:
        if arg.upper() == 'COUNT':
            continue
            print('Continue Argument: ' + arg)
        elif arg.upper() == 'BREAK':
            break
            print('Break Argument: ' + arg)
        print('Good Argument: ' + arg)

# using the while statement
def SecretNumber():
    gotIt = False
    while gotIt == False:
        one = int(input(("Type a number between 1 and 10: ")))
        two = int(input(("Type a number between 1 and 10: ")))
        if one >= 1 and one <= 10:
            if two >= 1 and two <= 10:
                print('Secret number is: ' + str(one * two))
                gotIt = True
                continue
        else:
            print("Incorrect second value!")
    else:
        print("Incorrect first value!")
    print("Try again!")


# Creating sets. Note: in python +3.11 sets are included already in the default python installation
# from sets import Set
SetA = set(['Red', 'Blue', 'Green', 'Black'])
SetB = set(['Black', 'Green', 'Yellow', 'Orange'])

