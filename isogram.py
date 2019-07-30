"""3)	An isogram (also known as a "nonpattern word") is a logological term for a word or phrase without a repeating letter.
 Write a python function to test, if a given word (passed as an argument) is an perfect isogram."""

str1: str = input ("Enter word: ")

str1: str = str1.lower()
for word in str1:
    if str1.count(word) >1:
        print(str1 + " :is not a perfect isogram")
        exit(0)

print(str1 + " :is a perfect isogram")

