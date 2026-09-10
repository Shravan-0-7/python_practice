def prime(x,n):
    for i in range (2,11):
        if(x*i == n):
            return False
        else:
            return True


n=int(input("Enter any number"))
ans=True
for i in range(2,n):
    if(prime(i,n) == False):
        ans=False
        
if (ans== True):
    print(n,"is an prime number")
else:
    print(n,"is not an prime number")
