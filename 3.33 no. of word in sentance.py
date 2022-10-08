n=[]
count=0
a=int(input("enter number of sentances:"))
for i in range(0,a):
    s=input("sentance=")
    n.append(s)
for j in n:
    s=j.split()
    count=max(count,len(s))
print(count)
