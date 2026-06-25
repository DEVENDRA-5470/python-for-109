# emp_list=[]
# for i in range(1,11):
#     emp_list.append(i)
# print(emp_list)

# print([i**2 for i in range(1,11)])
# print([i for i in range(1,11) if i%2==0])
# print([str(i)+":EVEN" if i%2==0 else str(i)+":ODD" for i in range(1,11)])

# emp_name=["aman","SHIVAM","shubham"]
# res=[n.lower() for n in emp_name]
# res=[n.upper() for n in emp_name]
# res=["-".join(n) for n in emp_name]
# print(res)

fruits_list=["apple","mango","papaya","banana","orange","grapes"]
user="p"
res=[i.upper() for i in fruits_list if user in i]
print(res)



