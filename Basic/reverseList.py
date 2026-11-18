n=int(input("Enter the size of list: "))
arr=[]
print("Enter the elements in array")
for i in range(0,n):
    x=int(input())
    arr.append(x)

print(arr[::-1])