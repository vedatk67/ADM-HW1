#1 -)ZIPPED!
# append each pair as a list into holder. then iterate over each of them and implement wanted function.
x = input().split()
holder = []
for i in range(int(x[1])):
    holder.append(input().split())
# to give zip function splitted list we use * here
for i in zip(*holder):
    i = map(float, i)
    print(sum(i) / int(x[1]))

#2 -)ATHLETE SORT

##thanks to the sorted function key attribute, we can sort by two different variable by the help of operator class. 
import math
import os
import random
import re
import sys

from operator import itemgetter

if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    arr = []
    for _ in range(n):
        innerlist = list(map(int, input().rstrip().split()))
        innerlist.append(_)
        arr.append(innerlist)

    k = int(input())
    sortedlist = sorted(arr, key=itemgetter(k, m))
    for i in sortedlist:
        print(*i[:-1])

#3 -)GINORTS
# ascii char have their ord value.So that i split them into small chunks and sort them within each other.And then collect them into one single list.
s = input()
lowercase = []
uppercase = []
digitsodd = []
digiteven = []
for i in s:
    if i.isdigit():
        if int(i) % 2 == 0:
            digiteven.append(i)
        else:
            digitsodd.append(i)
    elif i.islower():
        lowercase.append(i)
    elif i.isupper():
        uppercase.append(i)
lowercase = sorted(lowercase)
uppercase = sorted(uppercase)
digiteven = sorted(digiteven)
digitsodd = sorted(digitsodd)
for i in uppercase:
    lowercase.append(i)
for i in digitsodd:
    lowercase.append(i)
for i in digiteven:
    lowercase.append(i)

print("".join(lowercase))