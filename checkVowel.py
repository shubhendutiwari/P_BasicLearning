""" Write a function that takes a character (i.e. a string of length 1)
and returns True if it is a vowel, False otherwise"""

def checkVowel(checkChar):
    check=checkChar.lower()
    print(check)
    if check =="a" or check =="e" or check =="i" or check =="o" or check == "u":
        return True
    else:
        return False

char = input("Enter character : ")
print(checkVowel(char))
