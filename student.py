role = input("enter the role: ")
age= int(input("enter the age: "))

eligible = role.lower() == "student" and age<21

print("Eligible = ",eligible)