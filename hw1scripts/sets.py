#1 -)INTRODUCTION TO SETS
# takes distinct array ad return sum of them divided by total number of item


def average(array):
    arr = set(array)

    return sum(arr) / len(arr)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

#2 -)NO IDEA!

n, m = input().split()
nliste = input().split()
A = input().split()
B = input().split()
nliste = [int(i) for i in nliste]
# convert A to set
A = set([int(i) for i in A])
# Conver B to set
B = set([int(i) for i in B])
score = 0
# if conditions are okay do the related things.
for i in nliste:
    if i in A:
        score += 1
    elif i in B:
        score -= 1
    else:
        continue
print(score)

#3 -)SYMMETRIC DIFFERENCE
numlen = input()
liste = input().split()
numlen1 = input()
liste1 = input().split()

liste = set(liste)
liste1 = set(liste1)
setdif = liste.difference(liste1)
setdif1 = liste1.difference(liste)

holder = [int(i) for i in setdif]
for i in setdif1:
    holder.append(int(i))

holder.sort()

for i in holder:
    print(i)

#4 -)SET.ADD()

numberofex = input()

countries = set()
for i in range(int(numberofex)):
    x = input()
    countries.add(x)

print(len(countries))

#5 -)SET.DISCARD(),.REMOVE() &.POP()

n = int(input())
s = set(map(int, input().split()))
noffunc = int(input())
# with using gettatribute function we implement both methods and their arguments to class
for i in range(noffunc):
# some of them 1 argument some of them none. so to deal with it we use *args
    comment, *args = input().split()
    getattr(s, comment)(*(int(x) for x in args))

print(sum(s))

#6 -)SET.UNION() OPERATION

numofeng = int(input())
stueng = set(input().split())
numofrenh = int(input())
stufrench = set(input().split())

newset = stueng.union(stufrench)

print(len(newset))

#7 -)SET.INTERSECTION() OPERATION

s = int(input())
se = set(input().split())
b = int(input())
be = set(input().split())
newlist = list(se & be)
print(len(newlist))

#8 -)SET.DIFFERENCE() OPERATION

s = int(input())
se = set(input().split())
b = int(input())
be = set(input().split())
newlist = list(se.difference(be))
print(len(newlist))

#9 -)SET.SYMMETRIC_DIFFERENCE() OPERATION

s = int(input())
se = set(input().split())
b = int(input())
be = set(input().split())
newlist = list(se.symmetric_difference(be))
print(len(newlist))

#10 -)SET MUTATIONS

A = int(input())
se = set(input().split())
for i in range(int(input())):
    comment, numofelement = input().split()
    getattr(se, comment)(input().split())

print(sum(map(int, se)))

#11 -)THE CAPTAIN 'S ROOM

import collections

s = int(input())
c = collections.Counter(input().split())
print([i for i in c][-1])

#12 -)CHECK SUBSET

for i in range(int(input())):
    lengthA = int(input())
    setA = set(input().split())
    lengthB = int(input())
    setB = set(input().split())
    if setB & setA == setA:
        print(True)
    else:
        print(False)

#13 -)CHECK STRICT SUPERSET

setA = set(input().split())
holder = []
for i in range(int(input())):
    setB = set(input().split())
    if len(setA.difference(setB)) > 0 and len(setB.difference(setA)) == 0:
        holder.append(True)
    else:
        holder.append(False)

if False in holder:
    print(False)
else:
    print(True)

