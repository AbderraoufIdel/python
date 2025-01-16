def is_isogram(string):
    string = string.lower()
    string = "".join(char for char in string if char not in " -")
    return len(string) == len(set(string))
