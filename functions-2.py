# functions -2 

# def funcSum(a,c,b=10):  # default argument 
#     print(a+b)
    
# # funcSum(11)
# funcSum(11,15,33)

# def funcSums(*a):  # arbitrary arguments *args
#     print(a)
#     s=0
#     for i in a:
#         s+=i  # s=s+i
#     print(s) 
# funcSums(12,13)
# funcSums(12,13,45)
# funcSums(12,13,45,21)
# funcSums(12,13,45,21,10)



# def kwargsSum(**a): # abitrary keyword arguments **kwargs
#     print(a)
    
# kwargsSum(a=10,b=13,c=15)
# kwargsSum(a=10,b=13,c=15,d=34) 


# lambda function - single line function, anonymous function 
def sums(a,b):
    print(a+b)
    # return a+b 

# s=lambda a,b:print(a+b)
# s=lambda a,b:a+b 
# print(s(11,23))

oddEven= lambda a:"Even" if a%2==0 else "Odd"
print(oddEven(22))


