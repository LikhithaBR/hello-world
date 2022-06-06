a=input("Enter a value for a: ")
b=input("Enter a value for b: ")

def max(a,b):
    if(a>b):
        return True
    else:
        return False

if max(a,b)==True:
    print("a is greater than b")

else:
    print("a is not greater than b")