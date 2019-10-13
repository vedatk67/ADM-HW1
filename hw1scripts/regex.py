# 1-)DETECT FLOATING POINT NUMBER
import re

string = int(input())
my_regex = re.compile(r"^[+-.]?\d*\.[0-9]*$")
for i in range(string):
    strings = input()
    x = my_regex.search(strings)
    if x:
        print(True)
    else:
        print(False)

# 2-)RE.SPLIT()
regex_pattern = "[,.]"  # Do not delete 'r'.

import re

print("\n".join(re.split(regex_pattern, input())))

# 3-)GROUP(), GROUPS() & GROUPDICT()
# first select the related area and then iterate over stirng to make pairwise comparisson
import re

m = re.findall(r"([A-Za-z0-9]+)", input())

match = 0
for item in m:
    i = "_"
    for char in item:
        if char == i:
            print(char)
            match += 1
            break
        else:
            i = char
    if match == 0:
        print(-1)
# 4-)RE.FINDALL() & RE.FINDITER()

import re

my_regex = re.findall(
    r'[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]?([AEIOUaeiou]{2,})[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]',
    input())
if len(my_regex) == 0:
    print(-1)
for i in my_regex:
    print(i)

# 5-)RE.START() & RE.END()
string = input()
eofinteerest = input()
length2 = len(eofinteerest)
counter = 0
for i in range(len(string)):
    if string[i:i + length2] == eofinteerest:
        print((i, i + length2 - 1))
        counter += 1
if counter == 0:
    print((-1, -1))

# 6-)REGEX SUBSTITUTION

import re

for i in range(int(input())):
    string = input()
    my_regex = re.compile("(?<= )&&(?= )")
    my_regex2 = re.compile("(?<= )\|\|(?= )")
    string = my_regex.sub("and", string)
    string = my_regex2.sub("or", string)
    print(string)

# 7-)VALIDATING PHONE NUMBERS

import re

for _ in range(int(input())):
    string = input()

    my_regex = re.compile("[7-9]{1}[0-9]{9}$")

    if my_regex.search(string) and len(string) == 10:
        print("YES")
    else:
        print("NO")

# 8-)VALIDATING AND PARSING EMAIL ADDRESSES

import email.utils
import re

for i in range(int(input())):
    x = email.utils.parseaddr(input())
    x = email.utils.formataddr(x)
    my_regex = re.compile(r"<[^_\-.][\w\-_.]{1,20}@[^_0-9\-\.]{1,20}\.[^_0-9\.]{1,3}>$")
    if my_regex.search(x):
        print(x)

# 9-)HEX COLOR CODE

import re

my_regex = re.compile(r"#[0-9A-Fa-f]{3,6}")

for i in range(int(input())):
    string = input()

    if my_regex.search(string):
        if my_regex.search(string).start() != 0:
            liste = my_regex.findall(string)
            for item in liste:
                print(item.lstrip())

# 10-)VALIDATING UID


import re

my_regex = re.compile(r"(.*\d.*){3}([.*A-Z.*]){2}")
for _ in range(int(input())):
    string = "".join(sorted(input()))
    counter = 0

    if len(string) == 10:

        if my_regex.search(string):
            counter += 1

        if re.search(r"(.)\1", string):
            counter -= 1

    if counter == 1:
        print("Valid")
    else:
        print("Invalid")

# 11-)VALIDATING CREDIT CARD NUMBERS

import re

for i in range(int(input())):
    string = input()
    couter = 0
    if re.search("^[456]{1}[0-9]{3}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4}-?$", string):
        couter += 1
    string = string.split("-")
    string = "".join(string)

    if re.search(r"([0-9])\1{3}", string):
        couter -= 1

    if couter == 1:
        print("Valid")
    else:
        print("Invalid")

# 12 -) VALIDATING POSTAL CODES

regex_integer_in_range = r"^[1-9][0-9]{5}$"  # Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"  # Do not delete 'r'.

import re

P = input()

print(bool(re.match(regex_integer_in_range, P))
      and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)




