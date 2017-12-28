# A new system policy has been put in place that requires all accounts to use a passphrase instead of simply a password. A passphrase consists of a series of words (lowercase letters) separated by spaces.

# To ensure security, a valid passphrase must contain no duplicate words.

# For example:

# aa bb cc dd ee is valid.
# aa bb cc dd aa is not valid - the word aa appears more than once.
# aa bb cc dd aaa is valid - aa and aaa count as different words.
# The system's full passphrase list is available as your puzzle input. 
#How many passphrases are valid?

import os

def open_file():
  with open(os.path.join("/Users/ewelina/Documents/AC","ad_4_data.txt")) as f:
      lines = f.readlines()
  return lines

def process_lines(lines):
  for i in range(0, len(lines)):
    lines[i] = lines[i].replace("\n", "").replace("  ", " ").split(" ")
  return lines

def count_lines(lines):
  counter = 0
  for line in lines:
    if len(line) == len(set(line)):
      counter += 1
  return counter

### ANSWER ###
   # 386 #


