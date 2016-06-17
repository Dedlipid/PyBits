import time
def luc():
    try:
        n = input("How Many Lucas Numbers Do You Want? ")
        a = 2
        b = 1
        if n==0:
            print a
        elif n==1:
            print b
        elif n>1:
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
    except IOError:
        print "That was not a number please try again"
        luc()
luc()
time.sleep(100)
