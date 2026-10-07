# n = int(input("enter the number of rows: "))
# for i in range(n):
#     for j in range(i+1):
#         print(chr(65+j), end=" ")
#     print()

# n = int(input("enter the number of rows: "))
# for i in range(n):
#     for j in range(i+1):
#         print(chr(65+i), end=" ")
#     print()

# n = int(input("enter the number of rows: "))
# count=0
# for i in range(n):
#     for j in range(i+1):
#         print(chr(65+count), end=" ")
#         count+=1
#     print()


n = int(input("enter the number of rows: "))
for i in range(n):
    print("  "* (n-i+1), end=" ")
    for j in range(2*i-1):
        print(chr(65+j), end=" ")
    print()


