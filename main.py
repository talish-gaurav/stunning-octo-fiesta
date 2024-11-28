n = int(input("Enter number of rows : "))
for c in range(n):
    space = n-1
    for d in range(1,space):
        print(" ",end = "")
    for d in range(1,c):
        print(c,end="")
    print()