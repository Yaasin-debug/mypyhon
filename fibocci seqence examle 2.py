#fibocci seqence
number=float(input("enter your number:"))
a,b=1.1,2.5+1.5
for i in range (9):
   print(a,end=",")
   a,b=b,a+b
