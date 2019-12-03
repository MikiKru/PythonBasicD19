# tabliczka mnożenia
x = range(1,11)
for i in x:
    for j in x:
        print("%10s" % bin(i*j)[2:].zfill(10), end=" ")
    print()