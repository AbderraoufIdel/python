from typing import Union
import math

def score(x: Union[int, float], y: Union[int, float]) -> int:
    # Ensure inputs are real numbers
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError("x and y must be real numbers")

    # Calculate the distance from the origin
    distance = math.sqrt(x**2 + y**2)

    # Determine points based on distance
    if distance <= 1:
        return 10
    elif distance <= 5:
        return 5
    elif distance <= 10:
        return 1
    else:
        return 0
