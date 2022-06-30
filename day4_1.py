test_list = [{"fname": "abc01", "lname": "xyz02", "age": "32",
              "address": "111 xyz rd, abc city, MD, 21774"},
             {"fname": "abc02", "lname": "xyz02", "age": "32",
              "address": "112 xyz rd, abc city, MD, 21774"},
             {"fname": "abc02", "lname": "xyz02", "age": "43",
              "address": "113 xyz rd, abc city, MD, 21774"},
             {"fname": "abc03", "lname": "xyz02", "age": "22",
              "address": "114 xyz rd, abc city, MD, 21774"}
             ]

value = input("Enter value: ")
value1=input("Enter second value: ")


def FindRec(test_list, value,value1):
    count = 0
    for sub in test_list:

        if sub['fname'] == value:
            if sub['lname']==value1:
                count = count + 1



    return count


print(FindRec(test_list, value,value1))



