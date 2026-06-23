# file handling 
# text files,json files 

# read - r, write - w, append - a, new file create and write or read - x, r+ - read + append, w+ write + read 


# with open('f.txt','r') as f:
#     print(f.read())
    
# with open('f.txt','w') as f:
#     f.write("Hello Neeraj")
    
# with open('f.txt','a') as f:
#     f.write(" Class how are you")
    
# f= open('f.txt','r')
# print(f.read())
# f.close()

# with open('file.txt','x') as f:
#     f.write("Hi")

# with open('f.txt','r+') as f:
#     print(f.read())
#     # f.seek(2)
#     f.write("\nGood Evening")

with open('f.txt','w+') as f:
    f.write("Good Evening")
    f.seek(6)
    print(f.read())