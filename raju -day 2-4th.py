try:
    num = int(input("Enter the number:"))
    reversed_num = 0

    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
        
    print("Mirror image: " + str(reversed_num))

except ValueError:
    print("no special characters are  allowed raju only number are allowed")
