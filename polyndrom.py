# check_palindrome.py

# Replace this number with any number you want to check
number = 12321

# Convert the number to string
num_str = str(number)

# Check if the string is the same reversed
if num_str == num_str[::-1]:
    print(f"{number} is a palindrome!")
else:
    print(f"{number} is NOT a palindrome.")
