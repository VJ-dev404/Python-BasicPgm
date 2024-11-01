a = [10, 20, 30, 40, 50]

# Check if 30 exists in the list 
key = 30
flag = False

for val in a:
    if val == key:
        flag = True
        break

if flag:
    print("Element exists in the list")
else:
    print("Element does not exist")
