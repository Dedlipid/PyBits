def luc():
    n = input("How Many Lucas Numbers Do You Want? ")
    a = 2
    b = 1
    if n==0:
        print a
    elif n==1:
        print b
    elif n>=2:
        print a
        print b
        for x in range(2,n):
            c = a+b
            print c
            a=b
            b=c
    else:
        print "kabab"
luc()
