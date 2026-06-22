# . Write a program to find the sum of the digits of a given number.

# a=input("Enter number ")
# s=0
# for i in a:
#     i=int(i)
#     s+=i
# print(s)


#  Write a program for a number guessing game where the computer randomly selects a number between 1 and 100, and the user tries to guess it. The program should give hints if the guess is too high or too low.

import random 
number = random.randint(1,100)  # 1 and 100 both include
print(number)

l=['guava','mango','watermelon','grapes','litchi','banana']
print(random.choice(l))
print(random.choices(l))
print(random.choices(l))


# val=['rock','scissor','paper']
# computerChoice= random.choice(val)
# userchoice=input("rock/scissor/paper pick any one ")
