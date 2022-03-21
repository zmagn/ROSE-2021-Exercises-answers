https://github.com/RedHat-Israel/ROSE/blob/master/docs/course_materials/exercises/04_Compound_data_types/homework_list.md

# 1 - Create a list
list1 = []
list2 = list()
l1 = [2,3,4,5,6]
index = l1.index(6)
print('The index of 6 is',index)

l1.append(7)
l1.append(8)
print('After adding new numbers this is the new list' ,l1)
len(l1)
length = len(l1)
print('The length is' ,length)
#Or I can do this /////////////

print('The length is' ,len(l1))

lnum = [1]
#l1 = lnum + l1
print(l1)

#Or I can do this ///////
l1.reverse()
l1.append(1)
l1.reverse()
print(l1)

# 2 - Slicing a list
print(f'First 4 numbers of l1' ,l1[0:4:])
print(f'Last 4 numbers of l1' ,l1[-4::])
print(l1[20])
Traceback (most recent call last):
  File "lists.py", line 31, in <module>
    print(l1[20])
IndexError: list index out of range

#It means it's out of range because the max range for this is 8

# 3 - Update the list
l1.remove(4)
l1.remove(5)
print(l1)

l2 = [-1,-2,-3]
print(f'This is l2 list' ,l2)

l3 = l1 + l2
print(f'This is l1 and l2 together' ,l3)

l3.sort()
print(f'This is l3 list sorted numbers' ,l3)
print(f'Length l1:' ,len(l1) ,f'Length l2:' ,len(l2) ,f'Length l3:' ,len(l3))


