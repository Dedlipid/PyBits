def lucas_seq(n):
    if n==0:
        return 2       
    elif n==1:
        return 1
    elif n>1 :
        print lucas_seq(n-2)
        print lucas_seq(n-1)
        return lucas_seq(n-2)+lucas_seq(n-1)
    else:
        print"Dind't work"
def printlucas_seq():
    digits_wanted = input("How many Lucas Numbers do you want? ")
    for x in range(digits_wanted):
        print lucas_seq(x)
    print "There you go "+str(digits_wanted)+" Lucas Numbers"
printlucas_seq()

