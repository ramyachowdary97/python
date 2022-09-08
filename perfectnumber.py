try:
 n=int(input("enter the number"))
 sum=0
 for i in range(1,n):
     if(n%i==0):
         sum=sum+i
 if(sum==n):
     print("it is a perfect number")
 else:
     print("it is not a perfect number")
except ValueError:
    print("please enter a valid input")
    
