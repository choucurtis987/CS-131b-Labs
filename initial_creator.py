#2-9-19
# creates initials for name based on capital letters

def initials(name):
  solution = ''
  # the for loop loops through the letters in name:
  for letter in name:
      # the .isupper() method determines if letter is capitalized:
      if letter.isupper():
          PERIOD = '.'
          # the capital letters are added with a period then to the blank string "solution":
          solution += letter+PERIOD

  return solution
