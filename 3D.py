from array import *
from numpy import *
import matplotlib.pyplot as plt
import mpl_toolkits as mplot3d
from time import perf_counter

# program for 3D pure Dirichlets BC

l = int(input("length of region  "))
b = int(input("breath of region  "))
w = int(input("height of region  "))

hd = int(input("Number of divisions in length  "))
d = int(input("Number of divisions in breath  "))
c = int(input("Number of divisions in height  "))
err = float(input("enter the error value  "))

while (l / hd != b / d or b / d != w / c or w / c != l / hd):  
    # loop for checking if delta x,y and z are same if not again ask for inputs
    print("\n")
    print(
        "  select appropriate values for length,breath and no of divisions in lenght and breath "
    )

    print("\n")
    l = int(input("length of region  "))
    b = int(input("breath of region  "))
    w = int(input("height of region  "))

    hd = int(input("Number of divisions in length  "))
    d = int(input("Number of divisions in breath  "))
    c = int(input("Number of divisions in height  "))


N = int(input("value of temperature at North face "))
W = int(input("value of temperature at west face "))
S = int(input("value of temperature at south face "))
E = int(input("value of temperature at east face "))
F = int(input("value of temperature at front face "))
A = int(input("value of temperature at aft face "))

print("\n")

# Start the stopwatch / counter
start = perf_counter()

arr = zeros([c + 1, d + 1, hd + 1])  # making a zero matrix of the given no of divisions

# asssigning the boundary face values to the arr matrix
for ab in range(1, c):
    for bc in range(1, d):
        arr[ab][bc][hd] = E


for ab in range(1, c):
    for bc in range(1, d):
        arr[ab][bc][0] = W


for ab in range(1, c):
    for bc in range(1, hd):
        arr[ab][0][bc] = F

for ab in range(1, c):
    for bc in range(1, hd):
        arr[ab][d][bc] = A


for ab in range(1, d):
    for bc in range(1, hd):
        arr[0][ab][bc] = N


for ab in range(1, d):
    for bc in range(1, hd):
        arr[c][ab][bc] = S

# assigning the 8 corner points values

arr[0][0][0] = (N + F + W) / 3
arr[0][0][hd] = (N + F + E) / 3
arr[c][0][0] = (S + F + W) / 3
arr[c][0][hd] = (S + F + E) / 3
arr[c][d][hd] = (E + S + A) / 3
arr[c][d][0] = (S + A + W) / 3
arr[0][d][hd] = (N + E + A) / 3
arr[0][d][0] = (N + A + W) / 3

# assigning the 12 common edges values

for i in range(1, d):
    arr[0][i][hd] = (N + E) / 2

for i in range(1, d):
    arr[0][i][0] = (N + W) / 2

for i in range(1, c):
    arr[i][0][0] = (F + W) / 2

for i in range(1, c):
    arr[i][0][hd] = (F + E) / 2

for i in range(1, hd):
    arr[0][0][i] = (N + F) / 2

for i in range(1, hd):
    arr[c][0][i] = (F + S) / 2

for i in range(1, d):
    arr[c][i][0] = (W + S) / 2

for i in range(1, d):
    arr[c][i][hd] = (S + E) / 2

for i in range(1, hd):
    arr[0][d][i] = (N + A) / 2

for i in range(1, hd):
    arr[c][d][i] = (S + A) / 2

for i in range(1, c):
    arr[i][d][hd] = (E + A) / 2

for i in range(1, c):
    arr[i][d][0] = (W + A) / 2


# guess value
GUESS = (N + S + E + W + A + F) / 6
for i in range(1, c):
    for j in range(1, d):
        for k in range(1, hd):
            arr[i][j][k] = GUESS


# aprroximating by CD2 scheme
cnt = 0  # variable for checking accuracy
it1 = zeros([c + 1, d + 1, hd + 1])  # zero matrix for accuracy calculations before
it2 = zeros([c + 1, d + 1, hd + 1])  # zero matrix for accuracy calculations after
counter = (c - 1) * (d - 1) * (hd - 1)
no_of_iterations = 0

while (
    cnt != counter
):  # to check weather the no of values which are lesss than error value if not equal to counter value the again run the whole loop

    for i in range(c + 1):  # assigning zero it1 matrix with (K)th iteration values
        for j in range(d + 1):
            for k in range(hd + 1):
                it1[i][j][k] = arr[i][j][k]

    for i in range(1, c):  # for performing the calculations
        for j in range(1, d):
            for k in range(1, hd):
                arr[i][j][k] = (
                    arr[i - 1][j][k]
                    + arr[i + 1][j][k]
                    + arr[i][j - 1][k]
                    + arr[i][j + 1][k]
                    + arr[i][j][k - 1]
                    + arr[i][j][k + 1]
                ) / 6

    for i in range(c + 1):  # assigning zero matrix with (K+1)th iteration values
        for j in range(d + 1):
            for k in range(hd + 1):
                it2[i][j][k] = arr[i][j][k]

    no_of_iterations = no_of_iterations + 1
    cnt = 0
    for i in range(1, c):  # comapring (k) and (k+1)th values with allowable error value
        for j in range(1, d):
            for k in range(1, hd):
                if abs(it2[i][j][k] - it1[i][j][k]) <= err:
                    cnt = cnt + 1

                else:

                    break


print(arr)

print("the no of iterations = ", no_of_iterations)

# Stop the stopwatch / counter
stop = perf_counter()


print("Elapsed time during the whole program in seconds:", stop - start)
