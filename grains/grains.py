def square(number):
    # when the square value is not in the acceptable range        
    if number not in range(1,65):
        raise ValueError("square must be between 1 and 64")
    
    #chessboard is a list of numbers that doubles each time
    chessboard = []

    #adding the number of grains of wheat in each square
    x = 1
    for _ in range(64):
        chessboard.append(x)
        x = 2 * x
    
    return chessboard[number - 1]

def total():
    #the total of the grains in the chessboard

    total = 0
    for i in range(1,65):
        total = total + square(i)
    
    return total