""" Define a simple "spelling correction" function correct() that takes a string and sees to it that
1) two or more occurrences of the space character is compressed into one, and
2) inserts an extra space after a period if the period is directly followed by a letter.
E.g. correct("This   is  very funny  and    cool.Indeed!") should return "This is very funny and cool. Indeed!"."""

import re


def correct(inputString):
    #Removing extra spaces
    correctedString = re.sub ('\ +', ' ', inputString)

    #Putting extra space after period
    correctedString = re.sub ('\.', '. ', correctedString)

    print (correctedString)


inputString = "This   is  very funny  and    cool.Indeed!. But      you should.try  this also"

correct (inputString)
