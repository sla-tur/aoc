#!/usr/bin/env python
# coding: utf-8

# In[184]:
import re
import math
import cmath

buttons = {}
ready = {}
collective_tokens = set()
x = complex(0)

def solve(x, buttons):
    global ready
    
    if cmath.phase(x) > math.pi/2 or cmath.phase(x) < 0:
        return float('inf')
    if (x == complex(0)):
        return 0
    if x in ready.keys():
        return ready[x]
    best = float('inf')
    for token, movement in buttons.items():
        best = min(best, solve(x-movement,buttons)+token)
    ready[x] = best
    return best


# In[203]:


with open("aoc2024day13.txt", "r") as file:
    for line in file:
        line = line.strip()
        button_match = re.match(r"Button (\w): X\+(\d+), Y\+(\d+)", line)
        if button_match:
            #print("Reading button label")
            button_label = button_match.group(1)
            x_coord = int(button_match.group(2))
            y_coord = int(button_match.group(3))
            buttons[3 - 2*(ord(button_label) - ord('A'))] = complex(x_coord, y_coord)
            continue
        prize_match = re.match(r"Prize: X=(\d+), Y=(\d+)", line)
        if prize_match:
            #print("Reading prize label")
            x_coord = int(prize_match.group(1))
            y_coord = int(prize_match.group(2))
            x = complex(x_coord, y_coord)
        if not line:
            #print("Reading empty line")
            print(x)
            print(buttons)
            solution = solve(x, buttons)
            ready = {}
            print(solution)
            if solution == float('inf'):
                continue
            collective_tokens.add(solution)

print(sum(collective_tokens))

