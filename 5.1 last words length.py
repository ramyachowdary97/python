def lengthoflastword(a):
    l=0
    x=a.strip()
    for i in range(len(x)):
        if(x[i]==" "):
            l=0
        else:
            l+=1
    return l
string=input("Enter a string:")
print(lengthoflastword(string))
