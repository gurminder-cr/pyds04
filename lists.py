# lists 
# multiple data types store in one variables 
# []
# ordered or indexed 
# heterogenous 
# mutable - can change during run time

# l=[12,45,'hello','hi',4.44,True]
# print(l)
# print(type(l))

l=[13,15,11,9,98,76,44,56]
print(l)

# method to sort a list 
# l.sort()
# print(l)

# remove values from list 
# l.pop(4)
# l.pop(10)
# Remove and return item at index (default last).
# Raises IndexError if list is empty or index is out of range.

# print(l)

# l.remove(44)
# print(l)


# l.append(12)
# l.append([11,19])
# print(l)
# print(l[9][1]) 

# l.extend([33,22,44])
# print(l) 


# l1=[]
# for i in range(0,35):
#     if i%3==0:
#         l1.append(i)
        
# print(l1)

l.insert(2,100)
l.insert(2,[111,344])
print(l)

# l.clear()
# print(l)

# print(l.count(13))
# print(l.index(11))  # (11,5,len(l))


# print(len(l))

# slicing 
l2=[13,15,11,9,98,76,44,56]
print(l2)
print(l2[:]) # start stop step
print(l2[1:]) # start stop step
print(l2[2:5]) # start stop step
print(l2[2:9]) # start stop step
print(l2[::]) # start stop step
# print(l2[::-1]) # start stop step
print(l2[1:6:1]) # start stop step
print(l2[1:6:2]) # start stop step