sstr=input("Enter the char: ")
def find(str,sstr):
    str="abcdefmnacyxh"
    count=0
    i=0
    while i <len(str):
        if str[i]==sstr:
            count += 1

        i = i + 1
    print(count)



find(str,sstr)
