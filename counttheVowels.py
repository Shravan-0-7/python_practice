

# vowels = "aeiouAEIOU"
# count=0
# for i in s:
#     if i in vowels:
#         count+=1

# print(f"{s} has {count} vowels")

s=input("Enter the string: ")
vowels = "aeiouAEIOU"
count=0
hm={}
for i in s:
    if i in vowels:
        hm[i] = hm.get(i, 0) + 1

for i in hm:
    print(i," : ",hm[i])