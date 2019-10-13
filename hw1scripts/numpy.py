#1 -)ARRAYS
# reversing numpy array
import numpy


def arrays(arr):
    return numpy.array(arr, float)[::-1]


arr = input().strip().split(' ')
result = arrays(arr)
print(result)

#2 -)SHAPE AND RESHAPE
# reshaping with reshape function
import numpy

print(numpy.array(list(map(int, input().rstrip().split()))).reshape(3, 3))

#3 -)TRANSPOSE AND FLATTEN

import numpy

inputs = input().rstrip().split()
n = int(inputs[0])
m = int(inputs[1])
orginallist = []
for i in range(n):
    orginallist.append(list(map(int, input().rstrip().split())))

x = numpy.array(orginallist)
print(x.transpose(), x.flatten(), sep='\n')

#4 -)CONCATENATE

import numpy

inputs = list(map(int, input().rstrip().split()))
x = numpy.array([list(map(int, input().rstrip().split()))], dtype=numpy.int8)
for i in range(inputs[0] + inputs[1] - 1):
    y = numpy.array([list(map(int, input().rstrip().split()))])
    x = numpy.concatenate((x, y), axis=0)

print(x)

#5 -)ZEROSANDONES

import numpy

inputs = list(map(int, input().rstrip().split()))

print(numpy.zeros(inputs, dtype=numpy.int))
print(numpy.ones(inputs, dtype=numpy.int))

#6 -)EYEANDIDENTITY
import numpy

# by using replace function replace "0" by " 0"
x = str(numpy.eye(*map(int, input().rstrip().split()), dtype=numpy.float)).replace("0", " 0")
print(x.replace("1", " 1"))

#7 -)ARRAYMATHEMATICS
import numpy

string = input().rstrip().split()
list1 = []
list2 = []
for i in range(int(string[0])):
    [list1.append(int(item)) for item in input().rstrip().split()]
for i in range(int(string[0])):
    [list2.append(int(item)) for item in input().rstrip().split()]
# convert list to numpy array and reshape by the input
list1 = numpy.array(list1, dtype=numpy.int).reshape((int(string[0]), int(string[1])))
list2 = numpy.array(list2, dtype=numpy.int).reshape((int(string[0]), int(string[1])))

print(list1 + list2)
print(list1 - list2)
print(list1 * list2)
print(list1 // list2)
print(list1 % list2)
print(list1 ** list2)

#8 -)FLOOR, CEIL AND RINT

import numpy

inputs = numpy.array(list(map(float, input().rstrip().split())))
numpy.set_printoptions(sign=" ")
print(numpy.floor(inputs))
print(numpy.ceil(inputs))
print(numpy.rint(inputs))

#9 -)SUM AND PROD
import numpy

s, y = map(int, input().rstrip().split())
# just with single line
print(numpy.product(numpy.sum(numpy.array([input().rstrip().split() for _ in range(s)], dtype=numpy.int), axis=0)))

#10 -)MIN AND MAX

import numpy

s, y = map(int, input().rstrip().split())
# just with single line
print(numpy.max(numpy.min(numpy.array([input().split() for _ in range(s)], dtype=numpy.int), axis=1)))

#11 -)MEAN, VAR, AND STD

import numpy

s, y = map(int, input().rstrip().split())

x = numpy.array([list(map(int, input().split())) for _ in range(s)])
# for arranging printing numpy has set_printoption function
numpy.set_printoptions(sign=" ")

print(numpy.mean(x, axis=1), numpy.var(x, axis=0), numpy.around(numpy.std(x), decimals=12), sep="\n")

#12 -)DOT AND CROSS
import numpy

s = int(input())
x = numpy.array([list(map(int, input().split())) for _ in range(s)])
y = numpy.array([list(map(int, input().split())) for _ in range(s)])
print(numpy.matmul(x, y))

#13 -)INNER AND OUTER

import numpy

x = numpy.array(list(map(int, input().split())))
y = numpy.array(list(map(int, input().split())))

print(numpy.inner(x, y), numpy.outer(x, y), sep="\n")

#14 -)Polynomials
import numpy

print(numpy.polyval(list(map(float, input().split())), int(input())))

#15 -)LINEAR ALGEBRA
import numpy

s = int(input())
x = []
for i in range(s):
    x.append(input().split())
print(numpy.around(numpy.linalg.det(numpy.array(x, dtype=numpy.float)), decimals=2))

