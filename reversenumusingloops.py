try:
 n=int(input("enter the numbers"))
 org=n
 sum=0
 while(n>0):
     a=n%10
     sum=sum*10+a
     n=n//10
     print(a)
 if(n<0):
     print("enter a valid input")
except ValueError:
    print("please enter  a valid  input")
