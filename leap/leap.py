def leap_year(year):
    #first: In every year that is evenly divisible by 4.
    if year % 4 == 0:
        #we get all the leap years and non leap years "evenly divisible by 100"
        if year % 100 == 0 and year % 400 != 0:
            #here we excluded all the non leap years divisible by 100
            return False

        else:
            return True

    else:
        return False
    