total_user=int(input("enter the total no of users : "))
staff_user=int(input("enter the total no. of staff users :"))
if(total_user<=0 & staff_user<=0):
                      print("enter a valid input")
else:
    print("the total student users are : ")
    t_user=staff_user/3
    student_user=total_user-staff_user-t_user
    print(student_user)

    
                    
