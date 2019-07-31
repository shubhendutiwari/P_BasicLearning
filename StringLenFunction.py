"""Define your own function that computes the length of a given list or string."""

def strLen(word):
    count = 0
    for x in word:
        count = count+1
    return count

str1 = input("Enter the string : ")

print("Size of input string is : "+str(strLen(str1)))
