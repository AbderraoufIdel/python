def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    n = 1
    #the aliquat number
    aliquat_num = []
    while n < number:
        if number % n == 0:
            aliquat_num.append(n)
            n += 1
        else:
            n += 1

    #perfect
    if sum(aliquat_num) == number:
        return "perfect"
    elif sum(aliquat_num) > number :
        return "abundant"
    elif sum(aliquat_num) < number:
        return "deficient"
