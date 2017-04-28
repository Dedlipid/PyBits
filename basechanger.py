def f():
  n=int(raw_input("Enter number "))
  b=int(raw_input("Enter base "))
  temp = n
  temp2 = b
  l=[]
  if n == 0 :
    print "0 in any base is 0"
  else:  
    while n >0:
      l.extend([n % b])
      n  = (n - (n % b))/b
    l = l[::-1]
    de = ''.join(str(e) for e in l)
    de = int(de)
    print de
  c = raw_input("Press enter to run again")
  if c == "":
    f()
f()
