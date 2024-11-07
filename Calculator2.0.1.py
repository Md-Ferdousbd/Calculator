#Starting program with salutation!

print("Assalamualikum!")
print("Welcome to calculation with 'One calculator'!")
#User imput
num1= float(input("please enter first number: "))
symbol= input("please input symbol, + ,-,*,/")
num2= float(input("please enter second number: "))

#result
result= 0

#symbol to use
if symbol == '+':
    result = num1 + num2
elif symbol == '-':
    redult= num1-num2
elif symbol == '*':
    result= num1 * num2
elif symbol == '/':
    result= num1 / num2
else :
    result= 'Not allowed'


    # Print the result
print("The result is ", result)
print("Thank you for One_Calculator 2.0")
print(" Developed by One Software Farm ")

