def fibonacci(n):  
   if n <= 1:  
       return n  
   else:  
    return(fibonacci(n-1) + fibonacci(n-2))  

nth = int(input("enter total terms "))  
if nth <= 0:  
   print("enter positive integer")  
else:  
   print("Fibonacci sequence:")  
   for i in range(nth):  
       print(fibonacci(i)) 




  
