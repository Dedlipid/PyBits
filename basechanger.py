def f():
  n=int(raw_input("Enter number "))
  b=int(raw_input("Enter base "))
  l=[]
  if n == 0 :
    print "0 in any base is 0"
  else:
    while n > 0:
      l.extend([n % b])
      n  /= b
  l = l[::-1]
  if b <=10:
      l = ''.join(str(e) for e in l)
  else :
      l = ' '.join(str(e) for e in l)
  print l
  c = raw_input("Press enter to run again")
  if c == "":
    f()
f()

