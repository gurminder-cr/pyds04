# tuple - (), indexed, ordered, immutable 
a=(11,34,44,32,19)
print(type(a))

# t=(10,)
# print(t)
# print(type(t))
print(a)
print(a[:])

# a[1]=100
# print(a)

a=list(a)
# print(a)
a[1]=100
a=tuple(a)
print(a)


# sets - {} 
# sets - unordered, unique elements
print("--------------")
a={23,10,'hello',True,90,8.87,10,23}
print(a)

# value remove
# a.remove(901) #Remove an element from a set; it must be a member
# print(a)

a.discard(98) # Remove an element from a set if it is a member.
print(a)

a.pop()  # first value
print(a)
# print(a[2])  # []- subscriptable 

i={12,13,14,15,16}
j={13,14,18,19,20}
print(i.union(j))
print(i.intersection(j))
