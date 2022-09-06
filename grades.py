mark=[]
total=0
n=int(input("enter the total number of subjects"))
print("enter the  marks obtained in subjects")
for i in range(n):
    mark.append(input())
for i in range(n):
 total=total+int(mark[i])
average=total/n
print(average)
print(total)
if(average>=90):
    print("grade is A")
elif(average>=80):
    print("grade is B")
elif(average>=70):
    print("grade is C")
elif(average>=60):
    print("grade is D")
elif(average>=50):
    print("grade is E")
else:
    print("fail")
    

    
