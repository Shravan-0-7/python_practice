with open("logs.txt",'a') as f:
    f.write("program run successfully")

with open("logs.txt",'r') as f:
    data=f.read()
    print(data)