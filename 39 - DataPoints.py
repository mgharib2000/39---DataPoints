import numpy as np
import matplotlib.pyplot as plt

x = []
print("Enter 10 x coordinates: ")

for a in range(1, 11):
    xnumber = int(input("Enter x coordinate: "))
    x.append(xnumber)

y = []
print("Enter 10 y coordinates: ")
print(" ")

for b in range(1, 11):
    ynumber = int(input("Enter y coordinate: "))
    y.append(ynumber)

print(" ")

title = input("Enter title of graph: ")
xaxis = input("Enter x-axis label: ")
yaxis = input("Enter y-axis label: ")

plt.scatter(x, y)
plt.title(title)
plt.xlabel(xaxis)
plt.ylabel(yaxis)
plt.show()
