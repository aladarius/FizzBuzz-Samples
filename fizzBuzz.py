# Simple Fizz Buzz game in Python


def FizzBuzz():

    for index in range(1, 101):
        returnString = ""
        if(index % 3 == 0):
            returnString += "Fizz"
        if(index % 5 == 0):
            returnString += "Buzz"
        if(returnString == ""):
            returnString = str(index)

        print(returnString)

FizzBuzz()
