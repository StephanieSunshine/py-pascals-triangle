#!/usr/bin/env python3

# Pascals triangle
# 2022 Stephanie Sunshine -- MIT License

import colorama
from colorama import Fore
from colorama import Style

C = "A "
SEED = 3
ITERATIONS = 49
SCREEN_WIDTH = 160

class TNode:
    value = SEED
    parent_left = None
    parent_right = None

    def __init__(self, left = None, right = None):
        self.parent_left = left
        self.parent_right = right

    def calculate_value(self):
        tv = 0
        if self.parent_left is not None:
            tv += self.parent_left.value
        if self.parent_right is not None:
            tv += self.parent_right.value
        if tv != 0: self.value = tv

def fancy_print(r):
    # with ansi for color
    o = ""
    # without ansi for math
    oo = ""
    for e in r:
        oo += C
        if e % 7 == 0:
            o += Style.BRIGHT if e % 2 else Style.NORMAL
            o += Fore.WHITE+C
        elif e % 7 == 1:
            o += Style.BRIGHT if e % 2 else Style.NORMAL
            o += Fore.RED+C
        elif e % 7 == 2:
            o += Style.BRIGHT if e % 2 else Style.NORMAL
            o += Fore.BLUE+C
        elif e % 7 == 3:
            o += Style.BRIGHT if e % 2 else Style.NORMAL
            o += Fore.MAGENTA+C
        elif e % 7 == 4:
            o += Style.BRIGHT if e % 2 else Style.NORMAL
            o += Fore.YELLOW+C
        elif e % 7 == 5:
            o += Style.BRIGHT if e % 2 else Style.NORMAL
            o += Fore.GREEN+C
        else:
            o += Style.BRIGHT if e % 2 else Style.NORMAL
            o += Fore.CYAN+C
    # the ansi colors throw it off
    b = oo.rstrip().center(SCREEN_WIDTH)
    leading_white = len(b) - len(b.lstrip())
    print(f"{' '*leading_white}{o.rstrip()}")

colorama.init()

# make traversal easy
children = []

# row 1 has no parents
prev_row = [None, None]
for row in range(1,ITERATIONS+1):
    # first child created will never have a parent to the left just like the last one will never have a parent to the right
    current_row = [None]
    for node in range(0,row):
        child = TNode(prev_row[node], prev_row[node+1])
        current_row.append(child)
        child.calculate_value()
        children.append(child)
    prev_row = current_row
    prev_row.append(None)

row = []
for c in children:
    row.append(c.value)
    if c.parent_right is None:
        fancy_print(row)
        row=[]

