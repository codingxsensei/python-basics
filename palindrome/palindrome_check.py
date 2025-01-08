# Input a number from the user
num = int(input("Enter a number: "))

# Reverse the number
reversed_num = int(str(num)[::-1])

# Check if the original and reversed numbers are the same
if num == reversed_num:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")
