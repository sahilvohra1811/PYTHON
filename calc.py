a = int(input("Enter first number :"))
opr = input("Enter operator :")
b = int(input("Enter second number :"))

if(opr == '+'):
    print("sum is : ",a + b)
elif(opr == '-'):
    print("substraction is : ",a - b)
elif(opr == '*'):
    print("multiplication is : ",a * b)
elif(opr == '/'):
    print("division is : ",a / b)    
else:
    print("Enter valid operator.")
