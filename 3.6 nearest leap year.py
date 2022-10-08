inp_year = int(input("Give year:"))
year = inp_year
leap = year % 4 == 0 and year %100 != 0 or year % 100 == 0 and year % 400 ==0
if(leap):
    print(inp_year,"is an leap year.")
    print("The next leap year from",year,"is",year+4)
else:
    print(inp_year,"is not an leap year.")
    
    while not leap:
        year += 1
        leap = year % 4 == 0 and year %100 != 0 or year % 100 == 0 and year % 400 ==0
    print("The next leap year from",inp_year,"is",year)
