def give_sumof_range():
    try:

        n = raw_input('Two numbers please (with a comma in between): ')
        n=n.split(",")

        if n[0]>n[1]:
            i = int(n[0])
            j = int(n[1])
        else:
            i = int(n[1])
            j = int(n[0])

        result = (i*(i+1)) - (j*(j-1))
        print result/2

        give_sumof_range()
    except (IndexError,ValueError,ValueError):
        give_sumof_range()
give_sumof_range()



    


    
