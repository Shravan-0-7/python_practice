#replaceVowelInName.py

s=input("Enter you Name")

vowels="aeiou"

for i in s:
    if i.lower() in vowels:
        s=s.replace(i,"Z")

print(s)
