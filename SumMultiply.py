"""Define a function sum() and a function multiply() that sums and multiplies(respectively) all the numbers in a list 
of numbers. For example, sum([1, 2, 3, 4, 5]) should return 15, and multiply([1, 2, 3, 4]) should return 24"""

def sums(lsts):
    count =0
    for x in lsts:
        count = count+x
    return count
    
def multiply(lsts):
    mult = 1
    for x in lsts:
        mult=mult*x 
    return mult

lst=[]
n = int(input("Enter number of element you want to enter : "))
for i in range (0,n):
    print("Enter : "+ str(i+1)+" element")
    ele = int(input())
    lst.append(ele)
    
print("Sum is : "+str(sums(lst))+"& multiplication is : "+str(multiply(lst)))
