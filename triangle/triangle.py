def equilateral(sides):
    #first we need to sort the sides a, b, c
    a, b, c =sorted(sides)
    #rules: it's a triangle | and a=b=c
    return a == c > 0 #if the min value of sorted(sides)= the max value of sorted(sides) and > then 0 "a=b=c"


def isosceles(sides):
    #sides
    a, b, c = sorted(sides)
    #triangle | a + b > c | b = a or c
    return a + b > c and b in (a,c) and a > 0


def scalene(sides):
    #sides
    a, b, c = sorted(sides)
    #triangle | a<b<c | a+b>c
    return 0 < a < b < c < a + b
