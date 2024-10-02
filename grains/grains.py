def square(number):
    #chessboard is a list of numbers that doubles each time
    chessboard = []

    #adding the number of grains of wheat in each square
    x = 1
    for _ in range(64):
        chessboard.append(x)
        x = 2 * x
    
    return chessboard

def total():
    #the total of the grains in the chessboard
    
    total = 0
    for i in square(0):
        total = total + i
    
    return total