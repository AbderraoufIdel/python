def steps(number):
    #first we make sure that "number" is > 0
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    
    #now we do the math behind collatz conjecture
    #i: is no of steps
    i = 0

    #next we need to know if "number" is odd or even
    x = number % 2
    #if x = 0 "number" is even if not then "number" is odd

    if x == 0:
        while True:
            number = number / 2
            i += 1
            y = number % 2
            if number == 1 :
                break
            elif y != 0:
                number = number*3 + 1 
                i += 1
    else:
        while True:
            if number == 1 :
                break
            number = number*3 + 1 
            i += 1
            y = number % 2
            while y == 0:
                number = number / 2
                i += 1
                y = number % 2
    
    return i