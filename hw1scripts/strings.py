#1 -)SWAP CASE
# swap case function takes the input and control whether the char is lower or upper. If it is lower ,it makes it upper case vice versa
def swap_case(s):
    string = ""
    for letter in s:
        if letter.islower():
            string += letter.upper()
        else:
            string += letter.lower()

    return string


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

#2 -)STRING SPLIT AND JOIN
# this function first split by " " and join the list by "-"


def split_and_join(line):
    string = line.split(" ")
    string = "-".join(string)
    return string


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

#3 -)WHAT'S YOUR NAME?
# by format method we insert name and surname


def print_full_name(a, b):
    print("Hello {} {}! You just delved into python.".format(a, b))


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

#4 -)MUTATIONS
# strings are immutable so that we concatanate strings by not changing string itself.
def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

#5 -)FIND A STRING
# for substring to match with the string it must be within the lenght of string
# if string equal to sub string then increase counter by 1 and at final return counter
def count_substring(string, sub_string):
    lenofsub = len(sub_string)
    lenofstring = len(string)
    counter = 0
    for i in range(lenofstring):
        if lenofsub + i <= lenofstring:
            if string[i:i + lenofsub] == sub_string:

                counter += 1
            else:
                continue

    return counter


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)

#6 -)STRING VALIDATORS
# do the all necassary constraints in sequence.But for each condition use if else block

if __name__ == '__main__':
    s = input()
    alphanumerical = [1 if char.isalnum() else 0 for char in s]
    if sum(alphanumerical) > 0:
        print(True)
    else:
        print(False)
    alphabetical = [1 if char.isalpha() else 0 for char in s]
    if sum(alphabetical) > 0:
        print(True)
    else:
        print(False)
    digit = [1 if char.isdigit() else 0 for char in s]
    if sum(digit) > 0:
        print(True)
    else:
        print(False)
    lowercase = [1 if char.islower() else 0 for char in s]
    if sum(lowercase) > 0:
        print(True)
    else:
        print(False)
    uppercase = [1 if char.isupper() else 0 for char in s]
    if sum(uppercase) > 0:
        print(True)
    else:
        print(False)

#7 -)TEXT ALIGNMENT
# rjust allign like "     xyz"
# ljust allign like "xyz     "
# center allign like"   xyz  "
##Replace all ______ with rjust, ljust or center.

thickness = int(raw_input())  # This must be an odd number
c = 'H'

# Top Cone
for i in range(thickness):
    print(c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1)

# Top Pillars
for i in range(thickness + 1):
    print(c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6)

# Middle Belt
for i in range((thickness + 1) / 2):
    print(c * thickness * 5).center(thickness * 6)

# Bottom Pillars
for i in range(thickness + 1):
    print(c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6)

# Bottom Cone
for i in range(thickness):
    print((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(
        thickness * 6)

#8 -)TEXT WRAP

import textwrap
# textwrap returns list. wrap function retuning this list by joining them


def wrap(string, max_width):
    stri = textwrap.wrap(string, max_width)
    stri = '\n'.join(stri)
    return stri


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

#9-)DESIGNER DOOR MAT
##Comments are written below for necassary part
n, m = input().split(" ")
n = int(n)
m = int(m)
index = m // 2
index_constant = m // 2
basicshape = '-' * m
basicshape = [i for i in basicshape]
basicshape[index - 1:index + 2] = [".", "|", "."]
finallist = []
finallist.append("".join(basicshape))

for i in range(n // 2):
# this if part writes welcome part and append to finallist
    if i == n // 2 - 1:
        strings = ["W", 'E', "L", "C", "O", "M", "E"]
        newline = ["-" for s in range(m - 1)]
        newline[len(newline) // 2 - (len(strings) // 2):len(newline) // 2 + (len(strings) // 2)] = strings
        finallist.append("".join(newline))
# this part iteratively add .|. to the basicshape([-----*m]) to both right hand side and left hand side then append it to finallist
    else:
        index += 3 * (i + 1)
        basicshape[index - 1:index + 2] = [".", "|", "."]
        index -= (3 * (i + 1)) * 2
        basicshape[index - 1:index + 2] = [".", "|", "."]
        index = index_constant
        finallist.append("".join(basicshape))
# invert the list and then append it to final list because it will descent same way like upper part.
for i in finallist[::-1][1:]:
    finallist.append(i)
print("\n".join(finallist))

#10 -)STRING FORMATTING

# for every char implent rjust, spaces with the width of maximum binary number .


def print_formatted(number):
    width = int(bin(number)[2:])

    for i in range(number):
        octal = oct(i + 1)[2:]
        hexadecimal = hex(i + 1)[2:]
        binary = bin(i + 1)[2:]
        print(str(i + 1).rjust(width), octal.rjust(width), hexadecimal.rjust(width),
              binary.rjust(width), sep=" ")


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

#11-)ALPHABET RANGOLI


def print_rangoli(size):
    rangolidict = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h", 8: "i", 9: 'j',
                   10: 'k', 11: 'l', 12: "m", 13: 'n', 14: "o", 15: "p", 16: "q", 17: "r", 18: "s",
                   19: "t", 20: "u", 21: "v", 22: "w", 23: "x", 24: "y", 25: "z"}

    holder = []
    rowrightholder = []
    for i in range(size):
        rowrightholder.append(rangolidict[i])

    string = "-".join(rowrightholder[::-1])
    string1 = string[::-1][1:]
    result = string + string1
    reverselist = [i for i in range(size)][::-1]

    length = len(result)
    midpoint = length // 2
    placeholder = []
    for i in reverselist:
        midstr = "-" * length
        midstr = [z for z in midstr]
        midstr[midpoint] = rangolidict[i]

        placeholder.append(rangolidict[i])
        if len(placeholder) > 1:
            liste = [c for c in range(len(placeholder))][::-1]

            for another, c in zip(liste, range(len(liste))):
                midstr[midpoint + ((another) * 2)] = placeholder[c]
                midstr[midpoint - ((another) * 2)] = placeholder[c]
        holder.append("".join(midstr))
    holder2 = holder[::-1]
    for i in holder2[1:]:
        holder.append(i)

    print("\n".join(holder))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

#12 -)CAPITALIZE

## this function splits the char into list.
##every iteration it finds the next word index and append it to holder
## it capatilized chat that are found indexholder list
##returns the joint list

import math
import os
import random
import re
import sys


def solve(s):
    charholder = [i for i in s]
    indexholder = []
    charholder[0] = charholder[0].upper()
    for char, index in zip(charholder, range(len(charholder))):
        if index == len(charholder) - 1:
            break
        elif char == ' ' and charholder[index + 1] != " ":
            indexholder.append(index + 1)
    for indexes in indexholder:
        charholder[indexes] = charholder[indexes].upper()
    return "".join(charholder)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

#13 -)MERGETHE TOOLS!

# my algo choose firstelement to lastelement
# in this subset find the set and sort it by the orginal index
# increment firstelement and lastelement by k amount for next sub group
def merge_the_tools(string, k):
    lastelement = k
    firstelement = 0
    for i in range(int(len(string) / k)):
        eventofinterest = string[firstelement:lastelement]
        print(*sorted(set(eventofinterest), key=eventofinterest.index), sep="")
        firstelement += k
        lastelement += k

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

#14 -)THE MINION GAME
# for this task i write this code it works perfectly for test case but it gaves run time error when there is a long sequence of data
# so we must implent antoher cool mathematical way.
# Actually i found from discussion and i realy like the code. So i will describe it below.
import string
from collections import Counter


def minion_game(strings):
    vovels = set(["A", "E", "I", "O", "U"])
    consonants = set(string.ascii_uppercase).difference(vovels)
    holder = []
    strings = [i for i in strings]

    for i in range(1, len(strings) + 1):
        starting = 0
        ending = i
        x = True
        while x:
            holder.append("".join(strings[starting:ending]))
            starting += 1
            ending += 1
            if ending == len(strings) + 1:
                x = False
    stuart = 0
    Kevin = 0
    x = Counter(holder)
    for i in x:
        if i[0] in vovels:
            Kevin += x[i]
        else:
            stuart += x[i]
    if Kevin > stuart:
        print("Kevin", Kevin)
    elif Kevin < stuart:
        print("Stuart", stuart)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)


##2nd solution that i found from discussion. This one is logical.So that i want to use this one.
# for each char in string it looks whether it is vovels or not and if it is vovels it increase kevsc by the (len(s)-i) because there can be that much
# words can be created.
def minion_game(string):
    vowels = 'AEIOU'
    kevsc = 0
    stusc = 0
    for i in range(len(s)):
        if s[i] in vowels:
            kevsc += (len(s) - i)
        else:
            stusc += (len(s) - i)

    if kevsc > stusc:
        print("Kevin", kevsc)
    elif kevsc < stusc:
        print("Stuart", stusc)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
