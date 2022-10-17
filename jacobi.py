from array import *
from numpy import *
from matplotlib import pyplot as plt
from time import perf_counter


a = int(input("no of grid points  = "))
l = int(input("length of rod in meters= "))
b = int(input("value of temperature at left end in kelvins = "))
c = int(input("value of temperature at right end in kelvins= "))
E = float(input("enter the error value = "))

# to start the time for computing
start = perf_counter()

# initial guess
d = (b + c) / 2

# taking a empty array
arr = []


# adding intial guess and boundary values to the array arr
for i in range(a):
    if i == 0 or i == a - 1:
        if i == 0:
            arr.append(b)
        else:
            arr.append(c)

    else:
        arr.append(d)
print(arr)


cnt = 0
itt = []  # empty array
ab = zeros([a])  # array to store values before iteration
cd = zeros([a])  # array to store values after iteration
no_of_iterations = 0  # no of iterations counter


while cnt != a - 2:

    for q in range(0, a):  # to store values before iteration
        ab[q] = arr[q]

    for j in range(1, a - 1):  # calculating the values according to scheme
        itt.append((arr[j - 1] + arr[j + 1]) / 2)
    for q in range(0, a - 2):  # updating the old values by new values in arr
        arr[q + 1] = itt[q]

    no_of_iterations = no_of_iterations + 1  # iteration counter

    for r in range(0, a):  # to store values after iteration
        cd[r] = arr[r]

    cnt = 0

    for m in range(1, a - 1):
        if abs(cd[m] - ab[m]) <= E:
            cnt = cnt + 1

        else:
            break

    itt = []


print(arr)

print("\n")

print("no of iterations = ", no_of_iterations)


print("\n")

lengtha = []

for r in range(0, a):  # to make length array with respect to the temperature values
    lengtha.append((l / (a - 1)) * r)
print(lengtha)

plt.plot(lengtha, arr)  # plotting length and temperature values
plt.title("1D representation of temperature profile (jacobi iteration method)")

plt.xlabel("Length in m")
plt.ylabel("Temperature in K")

stop = perf_counter()  # stopping time counter

print("\n")

print("Elapsed time during the whole program in seconds:", stop - start)

plt.show()