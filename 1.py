print("Question1")
year=int(input("Enter year"))
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
             print("%d is a leap year" %year)
        else:
             print("%d is not a leap year" %year)
    else:
        print("%d is a leap year" %year)
else:
    print("%d is not a leap year" %year)
print('*'*10)
print('\n')
print("Question2")
length=float(input("Enter length"))
breadth=float(input("Enter breadth"))
if(length==breadth):
    print("Dimensions are of Square")
else:
    print("Dimensions are of rectangle")
print('*'*10)
print('\n')
print("Question3")
age1=float(input("Enter the age of first person"))
age2=float(input("Enter the age of second person"))
age3=float(input("Enter the age of third person"))
if((age1>=age2)and(age1>=age3)):
    print("%f is the oldest" %age1)
elif((age2>=age1)and(age2>=age3)):
    print("%f is the oldest" %age2)
elif((age3>=age1)and(age3>=age2)):
    print("%f is the oldest" %age3)
if((age1<=age2)and(age1<=age3)):
    print("%f is the youngest" %age1)
elif((age2<=age1)and(age2<=age3)):
    print("%f is the youngest" %age2)
elif((age3<=age1)and(age3<=age2)):
    print("%f is the youngest" %age3)
print('*'*10)
print('\n')
print("Question4")
points=float(input("Enter points"))
if(points<=200):
    if((points>=1) and (points<=50)):
        print("Sorry! No Prize.")
    elif((points>50) and (points<=150)):
         print("Congratulations! You won a Wooden dog.")
    elif((points>150) and (points<=180)):
         print("Congratulations! You won a Book.")
    elif((points>180) and (points<=200)):
         print("Congratulations! You won a Chocolate.")
else:
    print("Invalid input")
print('*'*10)
print('\n')
print("Question5")
quantity=float(input("Enter quantity"))
if((quantity*100)>1000):
    discount=0
    discount=(0.1*quantity*100)
    cost=0
    cost=(quantity*100)-discount
    print("Cost is %f" %cost)
else:
    print("Cost is",quantity*100)
