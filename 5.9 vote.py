age=(input("enter the age"))
try:
 if(age>=18):
     print("eligible")
 else:
     elig=18-age
     print("ur eligible after" ,elig ,"years")
except:
    print(" enter a valid input")
