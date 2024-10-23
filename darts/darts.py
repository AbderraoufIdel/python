from typing import Union
import math

def score(x: Union[int,float], y: Union[int,float]):
    if not isinstance(x,(int,float)) or not isinstance(y,(int,float)):
        raise TypeError("must be a real number")
    x = (x)*(x) 
    y = (y)*(y)
    points = 0
    distance = math.sqrt(x + y)

    if 0 <= distance <= 1:
        points += 10
    elif 1 < distance <= 5:
        points += 5
    elif 5 < distance <= 10:
        points += 1
    else:
        points += 0

    return points
