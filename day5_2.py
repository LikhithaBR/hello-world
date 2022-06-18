import os.path
f=open("C:/Users/Likhitha Bommilla/Desktop/demofile.txt","a")
Str=input("Enter the string to be appended to the file: ")
def file(f,Str):
    if os.path.exists("C:/Users/Likhitha Bommilla/Desktop/demofile.txt"):
        print("File exist")
        f.write(Str)
        f.close()
        f = open("C:/Users/Likhitha Bommilla/Desktop/demofile.txt", "r")
        if (f.read().__contains__(Str)):
            return True
        else:
            return False
    else:
        print("File not exist")


print(file(f,Str))




