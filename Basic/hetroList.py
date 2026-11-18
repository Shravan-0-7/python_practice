#hetroList.py

n = int(input("Enter the size of the List: "))
list=[]
for i in range(0,n):
    choice=input("Enter n for number and s for string: ")

    if choice=="n":
        value = int(input("Enter the number: "))
        list.append(value)
    else:
        value=input("Enter the string: ")
        list.append(value)

print("Orignal List: ",list)

numbers=[]
for i in list:
    if type(i)==int:
        numbers.append(i)

maximum=max(numbers)
indexofmax=list.index(maximum)

l1=list[:indexofmax]
l2=list[indexofmax:]

print("List before maximum:", l1)
print("List from maximum:", l2)


numbers.sort(reverse=True)  ## Descending order

print("Numbers in descending order:", numbers)

