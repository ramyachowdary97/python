a=float(input("enter the starting number:"))
b=int(input("max number of lines to be printed:"))
for i in range(b):
    for j in range(i+1):
        print('%.1f'%a,end=" ")
        a=a+0.1
    print()
