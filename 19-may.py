# What is function in python.
# 1.Every function has their own purpose.
# 2.Function is block of insturction(code) which execute inside its own block.
# 3.Fuction is reusable means define one time use manytime (DRY).
# 4.Function has two main part first functions defination second function calling.
# 5.In python bydefault function return None.

# How define function in python.
# 1.Take nothing return nothing.
# def add():
#     a=21
#     b=10
#     c=a+b
#     print(c)
# add()


# Function divide into 4 category.
# 1.Take nothing return nothing.
# 2.Take nothing return something.
# 3.Take somthing return nothing.
# 4.Take something return something

# Parameters(para) and arguments(args).
# Positional parameter/arguments
# Default parameter

# 3.Take somthing return nothing.
# def add(a=0,b=0):
#     print(a+b)
# add(11,22)

# def table_print(n):
#     for i in range(1,11):
#         print(f"{n} x {i} = {n*i}")
# m=2
# table_print(m)


# 3.Take somthing return nothing.
# def add(a=0,b=0):
#     print("Addition :",a+b)

# def sub(a=0,b=0):
#     print("Subtraction :",a-b)

# def mul(a=0,b=0):
#     print("Product :",a*b)

# def div(a=0,b=0):
#     print("Division :",a/b)

# num1=int(input("Enter number 1 :"))
# num2=int(input("Enter number 2 :"))
# opt=input("Choose option : + , - , * , / :")
# if opt=="+":
#     add(num1,num2)
# elif opt=="-":
#     sub(num1,num2)
# elif opt=="*":
#     mul(num1,num2)
# elif opt=="/":
#     div(num1,num2)
# else:
#     print("Shi se input")



# def add(a,b):
#     return a+b
# res=add(10,30)

# def sub(a,c):
#     return a-c
# print(sub(10,res))


def greet(a):
    return a
g=greet("Namaste")

def user_name(a):
    return a
u=user_name(input("Enter your name :"))

print(g,u)