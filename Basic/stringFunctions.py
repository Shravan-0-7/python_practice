s=input("Enter the string: ")

print(s.upper())    #prints the string in upper case
print(s.lower())    #prints the string in lower case

x=input(f"Enter the letter to count in {s} : ")
print(s.count(x))   #counts the occurrence of x in string S

print(f"before strip: {s}")
print(f"after strip: {s.strip() }")     #removes spaces from string from the both end


