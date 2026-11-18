a=5

n = int(input("Guess any number: "))
if(n>a):
    print("Guess is too high")
elif n<a:
    print("Guess is too Low")
else:
    print("CORRECT!")