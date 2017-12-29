# --- Day 13: Packet Scanners ---

# You need to cross a vast firewall. The firewall consists of several layers, each with a security scanner that moves back and forth across the layer. To succeed, you must not be detected by a scanner.

# By studying the firewall briefly, you are able to record (in your puzzle input) the depth of each layer and the range of the scanning area for the scanner within it, written as depth: range. Each layer has a thickness of exactly 1. A layer at depth 0 begins immediately inside the firewall; a layer at depth 1 would start immediately after that.

# For example, suppose you've recorded the following:

# 0: 3
# 1: 2
# 4: 4
# 6: 4
# This means that there is a layer immediately inside the firewall (with range 3), a second layer immediately after that (with range 2), a third layer which begins at depth 4 (with range 4), and a fourth layer which begins at depth 6 (also with range 4). Visually, it might look like this:

#  0   1   2   3   4   5   6
# [ ] [ ] ... ... [ ] ... [ ]
# [ ] [ ]         [ ]     [ ]
# [ ]             [ ]     [ ]
#                 [ ]     [ ]
# Within each layer, a security scanner moves back and forth within its range. Each security scanner starts at the top and moves down until it reaches the bottom, then moves up until it reaches the top, and repeats. A security scanner takes one picosecond to move one step. Drawing scanners as S, the first few picoseconds look like this:


# Picosecond 0:
#  0   1   2   3   4   5   6
# [S] [S] ... ... [S] ... [S]
# [ ] [ ]         [ ]     [ ]
# [ ]             [ ]     [ ]
#                 [ ]     [ ]

# Picosecond 1:
#  0   1   2   3   4   5   6
# [ ] [ ] ... ... [ ] ... [ ]
# [S] [S]         [S]     [S]
# [ ]             [ ]     [ ]
#                 [ ]     [ ]

# Picosecond 2:
#  0   1   2   3   4   5   6
# [ ] [S] ... ... [ ] ... [ ]
# [ ] [ ]         [ ]     [ ]
# [S]             [S]     [S]
#                 [ ]     [ ]

# Picosecond 3:
#  0   1   2   3   4   5   6
# [ ] [ ] ... ... [ ] ... [ ]
# [S] [S]         [ ]     [ ]
# [ ]             [ ]     [ ]
#                 [S]     [S]
# Your plan is to hitch a ride on a packet about to move through the firewall. The packet will travel along the top of each layer, and it moves at one layer per picosecond. Each picosecond, the packet moves one layer forward (its first move takes it into layer 0), and then the scanners move one step. If there is a scanner at the top of the layer as your packet enters it, you are caught. (If a scanner moves into the top of its layer while you are there, you are not caught: it doesn't have time to notice you before you leave.) If you were to do this in the configuration above, marking your current position with parentheses, your passage through the firewall would look like this:

# Initial state:
#  0   1   2   3   4   5   6
# [S] [S] ... ... [S] ... [S]
# [ ] [ ]         [ ]     [ ]
# [ ]             [ ]     [ ]
#                 [ ]     [ ]

# Picosecond 0:
#  0   1   2   3   4   5   6
# (S) [S] ... ... [S] ... [S]
# [ ] [ ]         [ ]     [ ]
# [ ]             [ ]     [ ]
#                 [ ]     [ ]

#  0   1   2   3   4   5   6
# ( ) [ ] ... ... [ ] ... [ ]
# [S] [S]         [S]     [S]
# [ ]             [ ]     [ ]
#                 [ ]     [ ]


# Picosecond 1:
#  0   1   2   3   4   5   6
# [ ] ( ) ... ... [ ] ... [ ]
# [S] [S]         [S]     [S]
# [ ]             [ ]     [ ]
#                 [ ]     [ ]

#  0   1   2   3   4   5   6
# [ ] (S) ... ... [ ] ... [ ]
# [ ] [ ]         [ ]     [ ]
# [S]             [S]     [S]
#                 [ ]     [ ]


# Picosecond 2:
#  0   1   2   3   4   5   6
# [ ] [S] (.) ... [ ] ... [ ]
# [ ] [ ]         [ ]     [ ]
# [S]             [S]     [S]
#                 [ ]     [ ]

#  0   1   2   3   4   5   6
# [ ] [ ] (.) ... [ ] ... [ ]
# [S] [S]         [ ]     [ ]
# [ ]             [ ]     [ ]
#                 [S]     [S]


# Picosecond 3:
#  0   1   2   3   4   5   6
# [ ] [ ] ... (.) [ ] ... [ ]
# [S] [S]         [ ]     [ ]
# [ ]             [ ]     [ ]
#                 [S]     [S]

#  0   1   2   3   4   5   6
# [S] [S] ... (.) [ ] ... [ ]
# [ ] [ ]         [ ]     [ ]
# [ ]             [S]     [S]
#                 [ ]     [ ]


# Picosecond 4:
#  0   1   2   3   4   5   6
# [S] [S] ... ... ( ) ... [ ]
# [ ] [ ]         [ ]     [ ]
# [ ]             [S]     [S]
#                 [ ]     [ ]

#  0   1   2   3   4   5   6
# [ ] [ ] ... ... ( ) ... [ ]
# [S] [S]         [S]     [S]
# [ ]             [ ]     [ ]
#                 [ ]     [ ]


# Picosecond 5:
#  0   1   2   3   4   5   6
# [ ] [ ] ... ... [ ] (.) [ ]
# [S] [S]         [S]     [S]
# [ ]             [ ]     [ ]
#                 [ ]     [ ]

#  0   1   2   3   4   5   6
# [ ] [S] ... ... [S] (.) [S]
# [ ] [ ]         [ ]     [ ]
# [S]             [ ]     [ ]
#                 [ ]     [ ]


# Picosecond 6:
#  0   1   2   3   4   5   6
# [ ] [S] ... ... [S] ... (S)
# [ ] [ ]         [ ]     [ ]
# [S]             [ ]     [ ]
#                 [ ]     [ ]

#  0   1   2   3   4   5   6
# [ ] [ ] ... ... [ ] ... ( )
# [S] [S]         [S]     [S]
# [ ]             [ ]     [ ]
#                 [ ]     [ ]
# In this situation, you are caught in layers 0 and 6, because your packet entered the layer when its scanner was at the top when you entered it. You are not caught in layer 1, since the scanner moved into the top of the layer once you were already there.

# The severity of getting caught on a layer is equal to its depth multiplied by its range. (Ignore layers in which you do not get caught.) The severity of the whole trip is the sum of these values. In the example above, the trip severity is 0*3 + 6*4 = 24.

# Given the details of the firewall you've recorded, if you leave immediately, what is the severity of your whole trip?

input = {
0: 4,
1: 2,
2: 3,
4: 5,
6: 8,
8: 4,
10: 6,
12: 6,
14: 6,
16: 10,
18: 6,
20: 12,
22: 8,
24: 9,
26: 8,
28: 8,
30: 8,
32: 12,
34: 12,
36: 12,
38: 8,
40: 10,
42: 14,
44: 12,
46: 14,
48: 12,
50: 12,
52: 12,
54: 14,
56: 14,
58: 14,
60: 12,
62: 14,
64: 14,
68: 12,
70: 14,
74: 14,
76: 14,
78: 14,
80: 17,
82: 28,
84: 18,
86: 14}

def prepare_dict(input):
    keys = list(input.keys())
    dct = {}
    sign = {}
    for key in keys:
        dct[key] = 1
        sign[key] = "+"
    return dct, sign

dct, sign = prepare_dict(input)

def count(input, dct, sign):
    position = -1
    counter = []
    answer = 0  
    keys_list = sorted(list(dct.keys()))

    while position <= keys_list[-1]:
        position += 1

        if position in dct:
          if dct[position] == 1:
              counter.append(position)

        for key in keys_list:
            if sign[key] == "+":
                dct[key] += 1
                # print("+", key, dct[key])
                if dct[key] == input[key]:
                    sign[key] = "-"   

            elif sign[key] == "-":
                dct[key] -= 1     
                # print("-", key, dct[key])         
                if dct[key] == 1:
                    sign[key] = "+" 
 
    for j in counter:
      answer += j * input[j]

    return answer


a= count(input, dct, sign)
print(a)

### ANSWER ###
  # 1904 #
