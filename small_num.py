a = [8, 3, 5, 1, 9, 12]

# Initialize "smallest" value with first element of list
smallest = a[0]

# Iterate through list to find smallest element
for val in a:
  
    # If current value is smaller than current smallest value
    if val < smallest:
      
        # Update the smallest value
        smallest = val

print(smallest)
