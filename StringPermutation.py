"""	Write a function which accepts a string and returns a list of all possible permutations of the given string in python. """

from itertools import permutations


def allPermutations(str):
    # Get all permutations of string 'ABC'
    permList = permutations (str)

    # print all permutations
    for perm in list (permList):
        print (''.join (perm))

    # Driver program


if __name__ == "__main__":
    str = 'ABCD'
    allPermutations (str)