def response(hey_bob):
    #"Sure." answer
    if hey_bob.rstrip().endswith("?"):
        #"Calm down, I know what I'm doing!" answer
        if hey_bob.isupper():
            return "Calm down, I know what I'm doing!"
        else:
            return "Sure."
    #"Whoa, chill out!" answer
    elif hey_bob.isupper():
        return "Whoa, chill out!"
    #"Fine. Be that way!"answer
    elif hey_bob.isspace() or hey_bob == "":
        return "Fine. Be that way!"
    #"Whatever."
    else:
        return "Whatever."