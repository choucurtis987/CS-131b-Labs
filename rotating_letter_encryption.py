# this function encrypts or decrypts a message(s) by rotating each letter in 
# the message by (n) through the alphabet. this is pretty much the caesar cipher 
# in a function. To decrypt a message use negative number.

# defines a function with 2 arguments 
# s = desired message to be encrypted
# n = number of rotation times // positive number encrypts and negative numbers can decrypt or encrypt:
def rot(s, n):
    # possible letter options alphabetically:
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # creates blank string:
    blank = ''
    # combats case sensitivity:
    s = s.upper()
    # loops through all letter in s:
    for letter in s:
        # determines if letter is in SYMBOLS:
        if letter in SYMBOLS:
            # finds the numeric value of that letter:
            x = SYMBOLS.find(letter)
            # adds the rotation number to the numeric value of that letter:
            new = x + n

            # if the number is greater than len(SYMBOLS): 
            if new >= len(SYMBOLS):
                # new number will be subtracted by len(SYMBOLS) to create a wraparound:
                new = new - len(SYMBOLS)

            # if the new number is less than zero:
            if new < 0:
                # new number will be added by len(SYMBOLS) to create a wraparound:
                new = new + len(SYMBOLS)
            # adds the new letter to a blank string:
            blank = blank + SYMBOLS[new]


        else:
            # if something in the message is not a letter it will simply be added to where it is suppose to be:
            blank = blank + letter


    # returns the blank string:
    return blank


