a=int(input("Enter your age:"))
#if statement no:1
if(a%2==0):
    print("a is even ")
#end of if statement no:1

#if statement no:2
if(a>18):
    print("Your are above the age of consent")
    print("Good for you ")

elif(a<0):
    print("You are entring an invalid negative number")

elif(a==0):
    print("You are entring 0 which is not valid ")

else:
    print("You are below the age of consent ")
#end of if statement no"2

print("End of program")