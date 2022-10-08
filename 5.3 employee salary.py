g=str(input("enter the grade of the employee(a/b):"))
s=int(input("enter the salary of the employee:"))
b=0
if s<=0:
    print("invalid input.")
if(g!='a' and g!='b'):
    print("invalid input")
elif g=='a':
    b=s*0.05
    print("salary:",s)
    print("bonus:",b)
    print("total to be paid:",s+b)
elif g=='b':
    b=s*0.10
    print("salary:",s)
    print("bonus:",b)
    print("total to be paid:",s+b)
elif s<10000:
    b=s*0.2
    print("salary:",s)
    print("bonus:",s-b)
    print("Total to be paid:",s+b)
else:
    print("enter a valid input.")
