''' List Implementation
def elementwise_greater_than(mylist, threshold):
    """Return a list with the same length as mylist, where the value at index i is 
    True if L[i] is greater than threshold, and False otherwise.
        >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
'''


def elementwise_greater_than(mylist, threshold):

    lst_out = []
    for x in mylist:
        if x > threshold:
            lst_out.append("true")
        elif x< threshold:
            lst_out.append("False")
        else:
            lst_out.append("equal")
    return lst_out



#empty list
lst =[]

#number of element in list
n= int(input("Enter the no of element : "))

for i in range(0,n):
     print("Enter "+str(i+1)+" element")
     ele = int(input())
     lst.append(ele)

threshold_value = int(input("Enter threshold_value : "))

print("Output : "+elementwise_greater_than(lst, threshold_value))
