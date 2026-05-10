a = int(input("Enter you age :"))
print("Your age is : ",a )
#conditional operator 
# >,<,>=,<=,==
# print((a>18))
# print((a<18))
# print((a>=18))
# print((a<=18))
# print((a==18))
# print((a!=18))
if(a>18):
    print("You can drive")
else:
    print("You can't drive")
print("I am outside the block")


applePrice = 10
budget = 200
if(applePrice<=budget):
    print("Alexa, add 1 kg apples to the cart")
elif(budget-applePrice>70):
    print("It's okay you can buy")
else:
     print("Alexa, don't add 1 kg apples to the cart")


num = int(input("Enter  the value of num : "))
if(num<0):
    print("Number is negative")
elif(num==0):
    print("Number is Zero")
elif(num==7):
    print("Number is Lucky")
else:
    print("Number is positive")

print("I am outside the block and I am happy")


num = 18
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")