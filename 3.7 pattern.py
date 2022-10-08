rows=int(input("enter no of rows:"))
k=(2*rows)-2

for i in range(1,rows):
    for j in range(0,k):
        print(end=' ')
    k=k-1
    for j in range(i,0,-1):
        print(j,end=' ')
    print(" ")
