a = int(input("Enter number one:")) 
b = int(input("Enter number two:")) 
c = int(input("Enter number three:")) 
if a > b and a > c:
    print(a, "is largest number")
elif b > a and b > c :
    print(b, "is largest number")
elif c > a and c > b :
    print(c, "is largest number")

if a < b and a < c:
    print(a ,"is smallest number")
elif b < a and b < c :
    print(b, "is smallest number")
elif c < a and c < b :
    print(c,"is smallest number")
