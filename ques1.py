a = [1, 11, 7, 8, -1, 6]
num=int(input("Enter the number:"))
def pos(a,num):
        if num in a:
            return a.index(num)
        else:
            return -1

print(pos(a,num))