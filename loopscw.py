#Problem 1
for i in range(-20,51,1):
    print(i)

#Problem 2
for x in range(0,21,2):
    print(x)

#Problem 3
num1=int(input("Enter number 1: "))
num2=int(input("Enter number 2: "))
num3= int(input("Enter number 3: "))
average= num1+num2+num3
print("The average of "+ str(num1)+ "," + str(num2)+" and,"+ str(num3)+ " is "+ str(average)+ "." )
#Problem 4
r=0
while(r<100):
    print(r)
    r+=4

#Challenege
userPW= input("Enter a Password: ")
userPWConfirm= input("Confirm Password or q to quit: ")
if(userPW==userPWConfirm):
    print("Password Correct")
else:
    print("You have exited the program")