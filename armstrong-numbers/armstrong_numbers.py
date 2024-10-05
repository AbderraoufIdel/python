def is_armstrong_number(number):
    #first: we need to know the no of digits of our "number"
    #i: is the no of digits
    x = y = number
    i = 0
    
    while x > 0:
        x //= 10
        i += 1
    
    #we have "i" as the no of digits of "number", now we do the math behind armstorng number
    #s: is the sum of each digit of "number" with the power of "i"
    s = 0
    while y > 0:
        digit = y % 10
        y //= 10
        s += pow(digit,i)
    
    #we have a problem here "number" = 0 after the last while func so we need to make a change

    if s == number:
        return True
    else:
        return False