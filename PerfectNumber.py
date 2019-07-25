"""Write a python function to test, if a given number (passed as argument) is a perfect number """

val: int = int(input("Enter the value"))
s: int = 0

for x in range(1, val-1):
    if val % x == 0:
        s += x
    else:
        continue

if s == val:
    print(str(val)+" is perfect number")
else:
    print(str(val)+" is not perfect number")