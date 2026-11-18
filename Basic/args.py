
# def new_fun(**mydict):
#     print("Argument type is: ",type(mydict))
#     print("Name: ",mydict["name"])
#     print("Age: ",mydict["age"])
#     print("All data: ",mydict)

# new_fun(name=" sds",age=36)


# def my_fun(*args):
#     print("First argument: ",args[0])
#     print("Second Argument: ",args[1])
#     print("All arguments: ",args[2])
#     print("\n Argument type is: ",type(args))

# my_fun(12,23," sdd")




# *args and **kwargs

# *args allows you to take a variable number of position-only arguments
def max_num(*num):
    if len(num) == 0:
        return None
    max_n = num[0] if isinstance(num[0], int) else len(num[0])
    for i in num:
        if isinstance(i, int):
            if i > max_n:
                max_n = i
        elif len(i) > max_n:
            max_n = len(i)
        else:
            pass
    print(max_n )
    return max_n



#max_num(23,-12,423,6,8,5,-21212)
max_num("Harshad", "piyuuuush", "Zara")


# **kwargs allows you to take a variable number of keyword-only arguments