def translate(text):
    #defining vowels , consonants
    vowels = "aeoiu"
    consonants = "bcdfghjklmnpqrstvwxyz"
    words = text.split(" ")
    word_count = 0
    for word in words:
    
        #Rule 1: "ay" sound 
        if any(word.startswith(vowel) for vowel in vowels) or word.startswith("xr") or word.startswith("yt"):
            word += "ay"

        #Rule 2: consonants & #Rule 3: "qu" & #Rule 4: "y"
        elif any(word.startswith(consonant) for consonant in consonants) or "qu" in word:
            consonant_count = 0
            couple_char = "qu"
            for char in word:
                if char in consonants:
                    consonant_count += 1
                    couple_char = couple_char[-1] + char
                elif char == "u" and "q" in couple_char:
                    consonant_count += 1
                    break
                else:
                    break
                if not word.startswith("y") and char == "y":
                    consonant_count -= 1
                    break
            word = word[consonant_count:] + word[:consonant_count] + "ay"
        word_count += 1  
        if word_count == 1:
            text = word
        elif word_count > 1:
            text += " " + word 
    text = text.rstrip()
    return text

print(translate("quick fast run"))