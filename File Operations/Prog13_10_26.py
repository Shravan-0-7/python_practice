# import os

# Write a program to read a file and count how many vowels are present in its content.
vowels="aeiou"
count=0
with open("file.txt",'r') as f:
    data = f.read()

    for ch in data.lower():
        if ch in vowels:
            count+=1
    print(f"There are {count} vowels in file.txt")


#Read all lines from a file into a list. Print the total number of lines and display the 2nd and 4th line.


# with open("file.txt",'r') as f:
#     lines=f.readlines()

# print("Total numbers of lines are",len(lines))
# if len(lines)>=2:
#     print("2nd Line: ",lines[1])
# if len(lines)>=4:
#     print("4th line: ",lines[3])


# sentence = input("Enter a sentence: ")
# words = sentence.split()
# longest = ""
# for word in words:
#     if len(word) > len(longest):
#         longest = word
# print("Longest word:", longest)



# with open("file.txt", "r") as f:
#     content = f.read()
# words = content.split()
# print("Total number of words:", len(words))
# unique_words = set(words)
# print("Unique words:")
# for word in unique_words:
#     print(word)




