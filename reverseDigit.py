n = int(input("Enter any Number: "))
reversed_digit =0 
while(n != 0):
    last = n%10
    reversed_digit = reversed_digit *10 + last
    n=n//10

print(" reversed digit is: ",reversed_digit)