import os.path

f = open("C:/Users/Likhitha Bommilla/Desktop/demofile.txt", "a")
Str = input("Enter the string to be added to the file: ")
def file(f,Str):


    f.write(Str)
    f.close()
    f = open("C:/Users/Likhitha Bommilla/Desktop/demofile.txt", "r")
    print(f.read())

    if(f==None):
        if(f.read()!=Str):
            return False
    else:

        return True

    f.close()

print(file(f,Str))



