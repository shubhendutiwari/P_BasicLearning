"""Define a function reverse() that computes the reversal of a string. """


def reverse(string1):
    print(string1)
    length = len(string1) - 1
    string2 = ""
    while length >= 0:
        string2 = string2 + string1[length]
        length = length - 1
    return string2


string = input("Enter the string for reversal : ")
print("Reverse for this string is : " + reverse(string))
