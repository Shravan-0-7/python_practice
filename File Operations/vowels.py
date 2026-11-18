with open("VOWELS.txt",'r') as f:
    data = f.read()
    count=0
    vowels="aeiou"
    for i in data:
        if i.lower() in vowels:
            count+=1
    print(f"There are {count} vowels in file: ")

