a=int(input("Enter the no of elements:"))
b=[]
for i in range(a):
    random_list=int(input("enter the number:"))
    b.append(random_list)
print("list of elements:")
frequency={}
for item in b:
    if item in frequency:
        frequency[item]+=1
    else:
        frequency[item]=1
print(frequency)
