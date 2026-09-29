original_n = int(input("Enter any Number: ")) 

n = original_n 
p = len(str(n))
sum = 0

while n != 0:
    last = n % 10
    sum += last ** p
    n = n // 10

if sum==original_n:
    print("The number is Armstrong")
else:
    print("The number is not Armstrong")
