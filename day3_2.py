
list1 = [1, 11, 7, 8, -1, 6 ,3]
def avg(list1):
    total = 0
    ele=0
    if(len(list1 )!=0):

        while ele < len(list1):
            total = total + list1[ele]

    else:
        return 0

    average =total /len(list1)
    return average



print(avg(list1))
