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
    print temp,"in base 10 is"
    for i in l:
      print i,
    print "in base",temp2
  c = raw_input("Run again?(y/n)")
  if c == "y":
    f()
f()
