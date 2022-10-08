a=int(input("enter the number of elements:"))
list1=[]
for i in range(0,a):
    c=int(input("enter the elements:"))
    list1.append(c)
print("list of elements :",list1)

d=int(input("enter the number of elements:"))
list2=[]
for i in range(0,d):
    e=int(input("enter the elements:"))
    list2.append(e)
print("list of elements :",list2)

sorted_list =[]
while list1 and list2:
    if list1[0] <  list2[0]:
        sorted_list.append(list1.pop(0))
    else:
        sorted_list.append(list2.pop(0))
sorted_list += list1
sorted_list += list2
print(sorted_list)
