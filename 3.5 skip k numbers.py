m=int(input("enter starting number of range:"))
n=int(input("enter the ending range:"))
k=int(input("enter thenumbers to be skipped in range:"))
if(m>n):
    print(m,"is lesser than",n,".It is an invalid input.")
elif(k<0):
    print(k,"it is an negative number,It is an invalid input.")
else:
    for i in range(m,n+1,k+1):
        print(i)
