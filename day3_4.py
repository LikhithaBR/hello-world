sstr=input("Enter the char: ")
def find(str,sstr):
    str="abcdefmnacyxh"
    count=0
    if sstr in str:
        count += 1
        return True

    else:
        return False

print(find(str,sstr))
