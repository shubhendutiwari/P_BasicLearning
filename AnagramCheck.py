"""Write a function which accepts a word and a list of words. Return the anagramsof that word from the given list
(as a list or return empty list if not found) Like print(my_anagram("ant", ["tan", "stand", "at"]))   prints [‘tan]"""

from collections import Counter

def anagram(ana_checks, lsts):
    ana_lst=[]
    for word in lsts:
        if Counter(ana_checks)==Counter(word):
            ana_lst.append(word)
        else:
            continue
    
    return ana_lst
    
lst = []

n=int(input("Enter number of element you want to enter in List : "))
for i in range (0,n):
    print("Enter : " +str(i+1)+ " word")
    word = input()
    lst.append(word)

ana_check=input("Enter the word for anagram check : ")
print("Result of anagram check : "+str((ana_check, lst)))
