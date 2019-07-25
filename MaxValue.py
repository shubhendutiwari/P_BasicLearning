"""Define a function max()that takes two numbers as arguments and
  returns the largest of them. Use the if-then-else construct available in Python."""

value1: int = int(input("Enter First number"))

value2: int = int(input("Enter Second number"))


def max_value(val1, val2):
    if val1 > val2:
        return val1
    else:
        return val2


print(str(max_value(value1, value2)) + " is max value")
