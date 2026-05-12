# Traversing of string using range()
name="python"
size=len(name)
for i in range(size):
    print(name[i],name,i)

# without range()
# name="python"
# for i in name:
#     print(i)


# for i in "python":
#     print(i)

# var1="DevOps Engineer"
# for i in var1:
#     if i=="e" or i=="E":
#         continue
#     print(i,end=" ")


# Wap to count all the voewls from give string : "this is devops batch".

str1="this is devops batch"
v_count=0
c_count=0
for i in str1:
    if i in "aeiou":
        v_count+=1
    else:
        c_count=c_count+1

# print(v_count)
# print(c_count)

# wap to print your name in reverse format.
name="PYTHON"
rev=""
for i in name:
    rev=i+rev
    print(rev)
    # ""="P"+""
    # "P"="Y"+"P"
    # "YP"="T"+"YP"
    # "TYP"="H"+"TYP"
    # "HTYP"="O"+"HTYP"
    # "OHTYP"="N"+"OHTYP"
    # "NOHTYP"
print(rev)


