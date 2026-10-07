

# vowels = "aeiouAEIOU"
# count=0
# for i in s:
#     if i in vowels:
#         count+=1

# print(f"{s} has {count} vowels")


s = input("Enter the string: ")
vowels = "aeiou"
count = 0
hm = {}

for i in s:
    if i.lower() in vowels:
        hm[i.lower()] = hm.get(i.lower(), 0) + 1
        count += 1

for i in hm:
    print(i, ":", hm[i])

print(f"{s} has {count} vowels")