
a=[]
for i in range(0,6):
    l=int(input())
    a.append(l)
print(a)
b=int(input("Enter number: "))


def check(a,b):
    if b in a:
        return a.index(b)
    else:
        return -1

print(check(a,b))
