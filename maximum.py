# Python program to find the
# maximum of two numbers

num_1 = int(input("Enter the first number :"))
num_2 = int(input("Enter the second number :"))

if (num_1 > num_2):
    print("Maximum =",num_1)
elif (num_1 < num_2):
    print("Maximum :",num_2)
else:
    print("Both are equal")   
    
    
# Python program to find the
# maximum of two numbers


def maximum(a, b):
    
    if a >= b:
        return a
    else:
        return b
    
# Driver code
a = 2
b = 4
print(maximum(a, b))
         