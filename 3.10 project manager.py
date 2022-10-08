def comb(L):
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if(i!=j and j!=k and i!=k):
                    print(L[i],L[j],L[k])
c1=int(input("enter first number:"))
c2=int(input("enter second number:"))
c3=int(input("enter third number:"))
comb([c1,c2,c3])
