with open("file.txt",'r') as f:
    data = f.readlines()
    print("No of line is: ",len(data))
    print("First line: ",data[1])
    print("Second line: ",data[0])