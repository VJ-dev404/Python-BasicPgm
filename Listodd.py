# Function to print odd numbers 
def print_odd_numbers(start, end):
    print(f"Odd numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if num % 2 != 0:
            print(num, end=' ')
    print()  

print_odd_numbers(1, 20)
