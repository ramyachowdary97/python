i=1
start = int(input("Enter the starting number of the range"))
end = int(input("Enter the ending number of the range"))
for j in range(start,end+1):
    while(i<=((j//2)+1)):
        if(i**2==j):
            print(j)
        i+=1    
    i=1
