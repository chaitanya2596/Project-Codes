from array import *
from numpy import *
import matplotlib.pyplot as plt
import mpl_toolkits as mplot3d
from time import perf_counter

# program for mixed BC, Neumann Boundary condiition at south bounary and rest all as Dirichlets Boundary condiition.

print("\n")

print(
    "Note that select length,breath and no of divisions in lenght and breath such that delta x and delta y shoould be same"
)

print("\n")

l = int(input("length of region  "))
b = int(input("breath of region  "))
c = int(input("Number of divisions on length  "))
d = int(input("Number of divisions on breath  "))
E = float(input("enter the error value  "))

while (
    l / c != b / d
):  # loop for checking if delta x and y are same if not again ask for inputs
    print("\n")

    print(
        "  select appropriate values for length,breath and no of divisions in lenght and breath "
    )

    print("\n")
    l = int(input("length of region  "))
    b = int(input("breath of region  "))
    c = int(input("Number of divisions on length  "))
    d = int(input("Number of divisions on breath  "))


north = int(input("value of temperature at North end  "))
west = int(input("value of temperature at west end  "))
east = int(input("value of temperature at east end  "))

print("\n")

# Start the stopwatch / counter
start = perf_counter()

arr = zeros([c + 1, d + 1])  # making a zero matrix of the given no of divisions

# assigning the bondary values to the zero matrix
for w in range(1, d):
    arr[0][w] = north

for x in range(1, c):
    arr[x][0] = west

for y in range(1, c):
    arr[y][d] = east

# assigning the corner values to the zero matrix
arr[0][0] = (north + west) / 2
arr[0][d] = (north + east) / 2

guess = (north + east + west) / 3

# assigning the guess values to the zero matrix
for e in range(1, c):
    for f in range(1, d):
        arr[e][f] = guess

# Neumann Boundary guess
for new in range(0, d + 1):
    arr[c][new] = (4 * (arr[c - 1][new]) - (arr[c - 2][new])) / 3

print(arr)

print("\n")


cnt = 0  # variable for accuracy

q = zeros([c + 1, d + 1])  # zero matrix for accuracy calculations
r = zeros([c + 1, d + 1])  # zero matrix for accuracy calculations
counter = (c + 1) * (d + 1)  # no of non boundary elements for accuracy check
no_of_iterations = 0

while (
    cnt != counter
):  # to check weather the no of values which are lesss than error value if not equal to counter value the again run the whole loop

    for ab in range(c + 1):  # assigning zero matrix with (K)th iteration values
        for cd in range(d + 1):
            q[ab][cd] = arr[ab][cd]

    for e in range(1, c):  # for performing the calculations
        for f in range(1, d):
            arr[e][f] = (
                arr[e - 1][f] + arr[e + 1][f] + arr[e][f - 1] + arr[e][f + 1]
            ) / 4

        for new in range(0, d + 1):
            arr[c][new] = (4 * (arr[c - 1][new]) - (arr[c - 2][new])) / 3

    no_of_iterations = no_of_iterations + 1

    for lm in range(c + 1):  # assigning zero matrix with (K+1)th iteration values
        for no in range(d + 1):
            r[lm][no] = arr[lm][no]

    cnt = 0
    for g in range(
        0, c + 1
    ):  # comapring (k) and (k+1)th values with allowable error value
        for h in range(0, d + 1):
            if abs(r[g][h] - q[g][h]) <= E:
                cnt = (
                    cnt + 1
                )  # counts the no of internal values whcih are in the limits

            else:

                break


print("final temperature values : ", arr)

print("\n")


print("the no of iterations = ", no_of_iterations)


# plotting


fig = plt.figure()
ax = plt.axes(projection="3d")

# matrices used to denote the x and y coordinates with respect to the lenght and breath
xmat = zeros([c + 1, d + 1])
ymat = zeros([c + 1, d + 1])

# this is for X values for
for qbo in range(c + 1):
    for ma in range(d + 1):
        xmat[qbo][ma] = (ma) * (b / d)


# this is for Y values
for abo in range(c, -1, -1):
    for yd in range(d + 1):
        ymat[abo][yd] = l - ((c - abo) * (l / c))

# plotting x,y and arr i.e. temperature values with respect to length and breath of slab
#ax.plot_surface(ymat, xmat, arr, cmap="turbo", edgecolor="green")
ax.plot_wireframe(ymat, xmat, arr, edgecolor="green")
ax.set_title("2D representation of temperature profile")

ax.set_xlabel("Length")
ax.set_ylabel("Breath")
ax.set_zlabel("Temperature")


# Stop the stopwatch / counter
stop = perf_counter()

print("\n")

print("Elapsed time during the whole program in seconds:", stop - start)

plt.show()