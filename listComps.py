# List comprehension 
# to create a new list from an existing iterable in a single line of code
l=[45,44,32,100,56,90]
# k=[i+5 for i in l]
# print(k)

# l1=[]
# for i in range(0,35):
#     if i%3==0:
#         l1.append(i)
#     else:
            # statemnt 
# print(l1)
# l1=[i for i in range(0,35) ]
# l1=[i for i in range(0,35) if i%3==0]
# print(l1)
# l1=[i**2 if i%5==0 else i for i in range(0,35)]
# print(l1)


a=[12,13,14,15,17]
b=[11,10,12,13,99,89]
# [12,13]

l=[]
# for i in a:
#     for j in b:
#         if i==j:
#             l.append(i)
# print(l)
# for i in a:
#     if i in b:
#         l.append(i)
# print(l)

# l=[i for i in a for j in b if i==j]
l=[i for i in a if i in b]
print(l)


