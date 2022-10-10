try:
    num1=int(input("enter 1st number:"))
    num2=int(input("enter 2nd number:"))
    print("after swapping:")
    print("A=",num2,"B=",num1)
except ValueError:
    print("enter only positive integers.")
