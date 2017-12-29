# --- Day 12: Digital Plumber ---

# Walking along the memory banks of the stream, you find a small village that is experiencing a little confusion: some programs can't communicate with each other.

# Programs in this village communicate using a fixed system of pipes. Messages are passed between programs using these pipes, but most programs aren't connected to each other directly. Instead, programs pass messages between each other until the message reaches the intended recipient.

# For some reason, though, some of these messages aren't ever reaching their intended recipient, and the programs suspect that some pipes are missing. They would like you to investigate.

# You walk through the village and record the ID of each program and the IDs with which it can communicate directly (your puzzle input). Each program has one or more programs with which it can communicate, and these pipes are bidirectional; if 8 says it can communicate with 11, then 11 will say it can communicate with 8.

# You need to figure out how many programs are in the group that contains program ID 0.

# For example, suppose you go door-to-door like a travelling salesman and record the following list:

# 0 <-> 2
# 1 <-> 1
# 2 <-> 0, 3, 4
# 3 <-> 2, 4
# 4 <-> 2, 3, 6
# 5 <-> 6
# 6 <-> 4, 5
# In this example, the following programs are in the group that contains program ID 0:

# Program 0 by definition.
# Program 2, directly connected to program 0.
# Program 3 via program 2.
# Program 4 via program 2.
# Program 5 via programs 6, then 4, then 2.
# Program 6 via programs 4, then 2.
# Therefore, a total of 6 programs are in this group; all but program 1, which has a pipe that connects it to itself.

# How many programs are in the group that contains program ID 0?

Your puzzle answer was 145.

import os

def open_file():
  with open(os.path.join("/Users/ewelina/Documents/AC","ad_12_data.txt")) as f:
      lines = f.readlines()
      input = {}
      for i in lines:
        a = i.split("<->")
        input[int(a[0])] = list(map(lambda x: int(x),a[1].rstrip().split(",")))
  return input

input = open_file()

def count(input):
  l = [0]
  z = [0]
  n = 0
  while n < len(input):
    print(n)
    for i in l:
      z.extend(input[i])
    l = list(set(z))   
    n += 1
  return len(l)

a = count(input)


# test_input = {
# 0 : [2],
# 1 : [1],
# 2 : [0, 3, 4],
# 3 : [2, 4],
# 4 : [2, 3, 6],
# 5 : [6],
# 6 : [4, 5]
# }
### TEST ANSWER ###
      # 6 #

### ANSWER ###
  # 145 #

