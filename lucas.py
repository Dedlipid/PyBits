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
            print b
            for x in range(2,n):
                c = a+b
                print c
                a=b
                b=c
        d = raw_input("Run again?(y/n)")
        if d == "y":
            luc()
    except NameError,SyntaxError:
        print "That was not a number please try again"
                
luc()
