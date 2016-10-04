#Simple Fizz Buzz game in Python

def FizzBuzz():
    
    for index in range(1, 100):
        count = 0;
        if(index % 3 == 0):
            print("Fizz")
            count = count + 1
        if(index % 5 == 0):
            print("Buzz")
            count = count + 1
        if(count == 2):
            print("FizzBuzz")
        elif(count == 0):
            print(str(index))
            

FizzBuzz()