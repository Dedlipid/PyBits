def f(num):
    steps = 0                                  
    if num == 1:
        print "steps = 0"
    if num == 0:
        print "Steps are infinite"
    if num >1:
        while num>1:
            if num % 2 ==0:
                num = num/2
                steps = steps +1
            else :
                num = num + 1
                steps = steps +1
        print "it took",steps,"Steps" 
def listmaker():
    list_begin=int(raw_input("From what number should the list start? "))
    list_end=int(raw_input("What should be the last item in the list? "))
    n = int(raw_input("at what interval?"))
    
    for x in range(list_begin,list_end+1):
        if x %n == 0:
            print "------------------THE NUMBER IS ",x,"------------------"
            f(x)
    get = raw_input("Run again?(y/n)")
    if get == "y":
        listmaker()
listmaker()
                    

