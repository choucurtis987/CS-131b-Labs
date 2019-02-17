# 2-15-19

# a function that returns the equal length anagrams of a word in a list

# opens the wordList file and reads through it and turns the file into a list:
with open('wordList.txt') as fd:
    # defines the list created:
    WORDS = fd.read().split()

# creates a function with input being the word u want to find anagrams of:
def anagram_finder(input):
    # sorts 'input' alphabetically:
    sorted_input = sorted(input)
    # creates a blank list:
    blank = []
    # loops through WORDS with enumeration:
    for number, word in enumerate(WORDS):
        # determines words in WORDS with equal length of 'input':
        if len(word) == len(input):
            # sorts 'word' of equal length to 'input' alphabetically:
            sorted_WORDS = sorted(word)
            # determines if sorted_input is equal to sorted_WORDS
            # if true then input has an equal length anagram because sorted_input
            # has the same words as sorted_WORDS:
            if sorted_input == sorted_WORDS:
                # gets the anagrams of a word by finding the corresponding enumerated 'number'
                # in WORDS and places this is the variable 'result':
                result = WORDS[number]
                # appends every anagram to the blank list result:
                blank.append(result)
    # returns the blank list with 'input' anagrams:
    return blank

# looking to update function to find words of unequal length within 'input'
