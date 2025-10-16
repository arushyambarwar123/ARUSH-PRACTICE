a = int(input("Enter Your Salary: "))
if a <= 10000 :
    print( "your new salary with bonus is :",a + a*0.1)

elif  a <= 20000 and a > 10000 :
    print( "your new salary with bonus is :",a + a*0.2)
      
elif  a <= 30000 and a > 20000 :
    print( "your new salary with bonus is :",a + a*0.3)

elif  a < 40000 and a > 30000 :
    print( "your new salary with bonus is :",a + a*0.4)
      
elif a >= 40000 :
    print("your new salary with bonus is :",a + a*0.5)
else:
    print("Sorry no salary bonus for you")

