startNumber=int(input(" enter the start range"))
endNumber=int(input(" enter the end range"))
prime = []
composite = []
for i in range(startNumber,endNumber):
        for p in range(2, i):
            if (i % p)==0:
                composite.append(i)
                break
        else:
            prime.append(i)
print("prime: ",prime)
print("composite: ",composite)
            
