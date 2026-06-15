# dictionary 
# - {} 
# key:value pairs 

l={'name':'Harjot','class':'btech','rollno':234,'isownapet':True}
print(l)
# print(l)
# print(type(l))

# s={}
# s1= set()
# print(type(s1))
# s1.update({12,33,44})
# print(s1)

# print(l['name'])
# # print(l['class'])
# # print(l['classs'])

# print(l.get('names',"key not present"))


# add in dictionary 
l['hobby']='gaming'
print(l)

l['class']='Btech CSE'
print(l)

l.update(age=21)
print(l)

l.pop('hobby')
# l.pop('hobby')
print(l)

print(l.keys())
print(l.values())
print(l.items())

# for i in l.items():
#     print(i)


for i,j in l.items():
    print(i,"--",j)
    
# dictionary comprehension 

print(l)
print({j:i for i,j in l.items()})