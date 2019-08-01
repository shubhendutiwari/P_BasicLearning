"""Write a python function to find the digital root of a number"""

digit = input("Enter the digit for digital root : ")
digit_root = 0
while len(digit) != 1:
    digit_root = 0
    for x in digit:
        digit_root = digit_root + int(x)

    digit = str(digit_root)

print("Digit root is : " + digit)