# Reverse string by using For loop

str = "Hello Duniya!"
reversed_string = " "
for char in str:
    reversed_string = char + reversed_string
print(reversed_string)    


# Reverse string by using Reversed Function

str = "Hii Coder!"
reversed_str = ''.join(reversed(str))
print(reversed_str)


# Reverse string by using Slicing

str = "Hii Python!"
reversed_str = str[::-1]
print(reversed_str)