# for i in range(0,3):
#     for j in range(0,i+1):
#         pr`int("*", end=" " )
#     print()

for i in range(1,6):
    if i%2==1:
        symbol="*"    
    else:
        symbol="#"
    space= 5-i
    stars = 2*i-1
    print(" "*space , symbol*stars)

