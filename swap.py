a=int(input("enter the value of a: "))
b=int(input("enter the value of b: "))
print(f"before swap a= {a}, b= {b}")
a+=b
b=a-b
a=a-b
print(f"after swap a= {a}, b= {b} \n")
