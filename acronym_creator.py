# creates an acronym based on all capital letters in word
def capital_acronym(word):
    answer = ''
    # the for loop loops through all the letters in word
    for letter in word:
        # the .isupper() method is a bool that determines if letter is uppercased
        if letter.isupper():
            # if letter is uppercased, it will add letter to the blank string "answer"
            answer += letter

    return answer
