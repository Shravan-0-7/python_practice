n=int(input("enter the size of n: "))
sum=0
for i in range(1,n):
    if i%2==0:
        sum+=i

print(sum)