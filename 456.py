def f(num):
    steps = 0                                  
    while num>1:
        if num % 2 == 0:
            num /= 2
            steps += 1
        else :
            num += 1
            steps += 1
    print "It takes",steps,"steps"

def listmaker():
    list_begin=int(raw_input("From what number should the list start? \n"))
    list_end=int(raw_input("What should be the last item in the list? \n"))
    n = int(raw_input("What number should they be a multiple of? \n"))
    for x in range(list_begin,list_end+1):
        if x % n == 0:
            print "------------------","THE NUMBER IS ",x,"------------------"
            f(x)
    get = raw_input("Run again?(y/n) \n")
    if get == "y":
        listmaker()

listmaker()

