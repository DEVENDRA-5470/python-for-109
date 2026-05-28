# Data Structure.
# Data structures used to store data effeciently and make faster process
# for operations like Read and write.

# 1.List : list()
# 2.String : str()
# 3.Dictionary : dict()
# 4.Set : set()
# 5.Tuple : tuple()

############################### 1.List
# 1.List is a data structure in python used to store multiple data of different types
# in one variable.
# 2.list can define by using square [] and data inside known as element.
# 3.list can be hetrogenous and homogenous.
# 4.list are mutable (changeable)
# 5.list support indexing ,slicing and follows ordering sequence.

# 1.list and its property
# 2.Creation of list.
# 3.Updation of list.
# 4.Indexing
# 5.Slicing
# 6.Traversing
# 7.In-built methods
# 8.Test
# 9.Assignments

# total index = length - 1
# marks_10th=[20,55,60,76,50,60,"hello",5.5]
# i=3
# print(marks_10th[i])
# # print("Before Update : ",marks_10th)
# data=marks_10th[2] # mutating list element using index.
# print(data)
# print("After Update : ",marks_10th)
# print(len(marks_10th))



# Slicing.
# marks=[10,20,30,40,50,60,70,80]
# [start-0:stop-1:step-1]
# sub_list=marks[6:0:-1]
# print(sub_list)

# 6.Traversing
# marks=[10,11,20,31,30,33,40,55,50,60,70,80]
# for i in range(len(marks)):
#     if marks[i]%2==0:
#         print(f"This elm is even : {marks[i]}")
#     else:
#         print(f"This elm is odd : {marks[i]}")


# marks=[10,11,20,31,30,33,40,55,50,60,70,80]
# for i in marks:
#     if i%2==0:
#         print(f"This elm is even : {i}")
#     else:
#         print(f"This elm is odd : {i}")


# marks=[10,11,20,31,30,33,40,55,50,60,70,80]
# total=0
# for i in marks:
#     total=total+i
# print(total)
