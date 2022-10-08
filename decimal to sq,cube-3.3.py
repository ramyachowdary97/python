num=float(input("enter any decimal number:"))
if(num<=0):
    print("invalid input")
else:
    square=num*num
    cube=square*num
    print("square for",num,"is:",square)
    print("cube for",num,"is:",cube)
