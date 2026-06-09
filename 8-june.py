# 7.In-built methods.
# append() : elements add to the last index.

emp_name=["aman","shivam"]
# new_emp="Kamal"
# print(emp_name)
# emp_name.append(new_emp)
# print(emp_name)
# new_emp1="rohan"
# emp_name.append(new_emp1)
# print(emp_name)

# emp_list=[]
# for i in range(1,11):
#     name=input("Enter your name : ")
#     emp_list.append(name)
# print("Updated list :",emp_list)

# emp_name=["aman","shivam"]
# print(emp_name)
# emp_name.append(["nma1","na2","n1",78,True,"noida"])
# print(emp_name[2][1])


# extend ()
# emp_name=["aman","shivam"]
# print(emp_name)
# emp_name.extend(["nma1","na2","n1",78,True,"noida"])
# print(emp_name)

# insert(position,value)
# emp_name=["aman","shivam"]
# print(emp_name)
# emp_name.insert(1,"IQ-INDIA")
# print(emp_name)

# pop() : default delete and return from last otherwise specific index.
# my_list=[100,200,300,400,500,600]
# d1=my_list.pop(3)
# print(my_list)
# print("Deleted element :",d1)

# remove()
# my_list=[100,200,300,400,500,600]
# r1=my_list.remove(200)
# print(my_list)
# print(r1)

# clear()
# my_list=[100,200,300,400,500,600]
# r1=my_list.clear()
# print(my_list)
# print(r1)

# reverse
# my_list=[100,200,300,400,500,600]
# my_list.reverse()
# print(my_list)

# sort()
# my_list=[10,2,33,4,500,600]
# my_list.sort(reverse=True)
# print(my_list)

# copy()
# my_list=[100,200,300,400,500,600]
# dup_list=my_list.copy()
# print(my_list)
# dup_list.pop(3)
# print(dup_list)

# index()
# my_list=[100,200,300,100,400,500,600]
# res=my_list.index(100,1)
# print(res)

# count()
# my_list=[100,200,300,400,100,500,600]
# res=my_list.count(100)
# print(res)

# universal.
my_list=[100,200,300,4000,100,500,600]
print(sum(my_list))
print(min(my_list))
print(max(my_list))
import math
print(math.prod(my_list))

my_list=[100,200,300,4000,100,500,600]
i=0
while i<len(my_list):
    print(my_list[i])
    i+=1



