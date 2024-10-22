
def is_palindrome(string):
    
    cleaned_string = ''.join(char.lower() for char in string if char.isalnum())
    
    return cleaned_string == cleaned_string[::-1]


input_string = input("Enter a string to check for palindrome: ")

if is_palindrome(input_string):
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")
