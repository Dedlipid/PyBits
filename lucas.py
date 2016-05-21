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
        print
        print b
        print
        for x in range(2,n):
            c = a+b
            print c
            print
            a=b
            b=c
    else:
        print "kabab"
luc()
