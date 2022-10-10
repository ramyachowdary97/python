rows=int(input("enter noof rows:"))
s=input("enter any symbol:")
for i in range(rows):
    for j in range(i+1):
        print(s ,end=" ")
    print("\n")
