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


# def greet(a):
#     return a

# def user_name(a):
#     return a


# print(greet("Namaste"),user_name(input("Enter your name :")))






"Hello Dev"
# total 2 function
# arg and parameter



# Waf to check number pass by argument is odd or even.
# def odd_even(a):
#     if a%2==0:
#         print("Even")
#     else:
#         print("Odd")
# odd_even(7)

# waf to check which number is greater and two number by user.
# def check_greater(n1,n2):
#     if n1 > n2 :
#         print(n1 ,"is greater")
#     else:
#         print(n2," is greater")

# n1=11
# n2=33
# check_greater(n1,n2)

# Waf to check the character pass by user is vowel or consonant.
# def check_char(c):
#     if c in "aeiouAEIOU":
#         print(f"Char is {c} vowel")
#     else:
#         print(f"This is consonant : {c}")

# user_input="k"   
# check_char(user_input)

# Waf to check is number completly divide by 2 and 3 and return 
# "Yes number is completely divide"
# "No number is not completely divide"
# def check_number(n):
#     if n % 2 == 0 and n % 3 == 0:
#         return "Yes number is completely divide"
#     else:
#         return "No number is not completely divide"
# res=check_number(6)
# print(res)

# waf to return length of a string pass by user without using len().
# def len_string(s):
#     print(s)
#     c=0
#     for i in s:
#         c+=1
#     return c
# res=len_string("python")
# print(res)
