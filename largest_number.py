def max():
    a = int(input("enter number:"))
    b = int(input("enter number:"))
    c = int(input("enter number:"))

    if ((a>c) & (a>b)):
        print("a is largest",a)
    elif ((b>a) & (b>c)):
        print("b is largest",b)
    else:
        print("c is largest",c)

max()
