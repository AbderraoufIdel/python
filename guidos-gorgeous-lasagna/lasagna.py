"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


# define the 'EXPECTED_BAKE_TIME' constant.
EXPECTED_BAKE_TIME = 40  # in minutes

# Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):

    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    time_remaining = EXPECTED_BAKE_TIME - elapsed_bake_time
    return time_remaining
    

# Define the 'preparation_time_in_minutes()' function below.
# You might also consider using 'PREPARATION_TIME' here, if you have it defined.
PREPARATION_TIME = 2  # in minutes

def preparation_time_in_minutes(number_of_layers):

    """Calculate the preparation time in minutes.

    :param number_of_layers: int - number of layers in lasagna.
    :return: int - preparation time in minutes derived from the number of layers.

    """
    time = number_of_layers * PREPARATION_TIME
    return time

# define the 'elapsed_time_in_minutes()' function below.
# Remember to add a docstring (you can copy and then alter the one from bake_time_remaining.)

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):

    """Calculate the total elapsed cooking time.

    :param number_of_layers: int - number of layers in lasagna.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - total elapsed time in minutes.

    Function that takes two numbers representing the number of layers & the time already spent baking
    and calculates the total elapsed minutes spent cooking the lasagna.
    """
    time = preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    return time