# 5.Membership opr (in , not in)

# str1="this is python for devops 109"
# find="109"
# print(find in str1)

# num1="4567"
# print("4" not in num1)

# email="iqindia123@gmail.com"
# find="@gmail.com"
# if find in email:
#     print("This is valid google mail id")
# else:
#     print("Invalid Email")


# aman_age=50
# abhisek_age=30
# if aman_age > abhisek_age:
#     print("Yes aman's age in more than abhisek")
# else:
#     print("No aman's age is not more than abhisek")


# user is eligble for voting.
min_age=18
nationality="IN"
user_age=int(input("Enter Your Age : "))
user_id=input("Enter Your Identiy (ex.IN) : ")
if user_age >= min_age and user_id==nationality:
    print("User is Eligible for voting")
else:
    print("User is not Eligible for voting")
