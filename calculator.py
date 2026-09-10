a =int(input("enter the value of a: "))
b=int(input("enter the value of b: "))
opr=input("Enter the operation to be performed")

match (opr):
    case '+':
        print(f"addition of {a} & {b} is: ",a+b)
        
     
    case '-':
        print(f"substraction of {a} & {b} is: ",a-b)
        

    case '*':
        print(f"multiplication of {a} & {b} is: ",a*b)
        

    case '/':
        print((f"division of {a} & {b} is: ",a/b))
        
