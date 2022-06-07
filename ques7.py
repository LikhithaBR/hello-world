a = [1, 11, 7, 8, -1, 6]


def even_max(a):
    evenlist = []
    for i in a:
        if i % 2 == 0:
            evenlist.append(i)
            return evenlist

            max = evenlist[0]

    for x in evenlist:
        if x > max:
            max = x
            return max


print(even_max(a))






