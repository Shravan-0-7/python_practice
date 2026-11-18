# def addition(a,b):
#     return a+b

# print(addition(10,20))

# def my_decorator(func):
#     def wrapper():
#         print("start")
#         func()
#         print("End")

#     return wrapper

# @my_decorator
# def hello():
#     print("hello")

# hello()


# def repeat(n):
#     def my_decorator(func):
#         def wrapper(*args,**kwargs):
#             for _ in range(n):
#                 func(*args)
#         return wrapper
#     return my_decorator

# @repeat(3)
# def gretting(name):
#     print(name)

# gretting("Shravan")






# def evenNos(n):
#     i = 1
#     while i<n:
#         yield i
#         i+=1

# x=evenNos(10)
# print(next(x))



# def feb(n):
#     a=0
#     b=1
#     i=0
#     while i<n:
#         yield a
#         a,b=b,a+b
#         i+=1

# x=feb(10)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))





# a = [1, 2]
# b = a
# b.append(3)
# print(a)



def table(x):
    i=1
    while True:
        yield i*x
        i+=1

t=table(3)


for i in range(10,0,-2):
    print(i)