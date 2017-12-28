# --- Day 8: I Heard You Like Registers ---

# You receive a signal directly from the CPU. Because of your recent assistance with jump instructions, it would like you to compute the result of a series of unusual register instructions.

# Each instruction consists of several parts: the register to modify, whether to increase or decrease that register's value, the amount by which to increase or decrease it, and a condition. If the condition fails, skip the instruction without modifying the register. The registers all start at 0. The instructions look like this:

# b inc 5 if a > 1
# a inc 1 if b < 5
# c dec -10 if a >= 1
# c inc -20 if c == 10
# These instructions would be processed as follows:

# Because a starts at 0, it is not greater than 1, and so b is not modified.
# a is increased by 1 (to 1) because b is less than 5 (it is 0).
# c is decreased by -10 (to 10) because a is now greater than or equal to 1 (it is 1).
# c is increased by -20 (to -10) because c is equal to 10.
# After this process, the largest value in any register is 1.

# You might also encounter <= (less than or equal to) or != (not equal to). However, the CPU doesn't have the bandwidth to tell you what all the registers are named, and leaves that to you to determine.

# What is the largest value in any register after completing the instructions in your puzzle input?

import os

def open_file():
  with open(os.path.join("/Users/ewelina/Documents/AC","ad_8_data.txt")) as f:
      lines = f.readlines()
  return lines

input = open_file()

def answer(a,b,o):
    m = None
    if o == ">":
        m = a > b
    if o == "<":
        m = a < b
    if o == "<=":
        m = a <= b
    if o == ">=":
        m = a >= b
    if o == "==":
        m = a == b
    if o == "!=":
        m = a != b
    return m 

def result(a,b,o):
    m = 0
    if o == "dec":
        m = a - b
    if o == "inc":
        m = a + b
    return m 

def find_max(input):
    d = {}
    arr = [element.split(' ') for element in input]
    for ar in arr:
        a = ar[0]
        b = ar[4]
        operator1 = ar[5]
        value1 = int(ar[6])       
        
        if a in d:
            va = d[a]    
        else: 
            va = 0
        
        if b in d:
            vb = d[b]    
        else: 
            vb = 0
        print(va, vb)

        if answer(vb, value1, operator1):
            operator2 = ar[1]
            value2 = int(ar[2])
            c = result(va, value2, operator2) 
            print("c: {}".format(c))         
            d[a] = c

    m = max(list(d.values()))
    return m
    
a = find_max(input)


### ANSWER ###
   # 5215 #

### TEST ###
# input = ['b inc 5 if a > 1', 'a inc 1 if b < 5', 'c dec -10 if a >= 1', 'c inc -20 if c == 10']

### TEST ANSWER ###
      # 1 #
