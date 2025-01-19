def reverse(text):
    reversed_text = ""
    x = 1

    while x <= len(text):
        reversed_text += "".join(text[-x])
        x += 1
    return reversed_text