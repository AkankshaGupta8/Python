#Write a program using functions to find greatest of three numbers. 

a=1
b=5
c=8

def greatest (a,b,c):
    if(a>b and a>c):
        return a

    elif(b>a and b>c):
        return b 
    elif(c>a and c>b):
        return c
    
a=1
b=5
c=8

print(greatest(a,b,c))