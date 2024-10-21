def convert(number):
    #first we need to define the string "raindrops"
    raindrop = ""
    # the "Pling" sound
    if number % 3 == 0:
        raindrop += "Pling"
    if number % 5 == 0:
        #the "Plang" sound
        raindrop += "Plang"
    if number % 7 == 0:
        #the  "Plong" sound
        raindrop += "Plong" 
    if not raindrop:
        raindrop = str(number)
    return raindrop