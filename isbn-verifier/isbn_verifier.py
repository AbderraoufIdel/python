def is_valid(isbn):
    isbn_digits = []
    for char in isbn:
        if char.isdigit():
            isbn_digits.append(int(char))
        elif char.upper() == 'X' and len(isbn_digits) == 9:
            isbn_digits.append(10)
        elif char.isspace() or char == '-':
            continue
        else:
            return False
    if len(isbn_digits) != 10:
        return False
    
    sum = 0
    d = 10
    for digit in isbn_digits:
        sum += digit * d
        d -= 1
    return sum % 11 == 0
