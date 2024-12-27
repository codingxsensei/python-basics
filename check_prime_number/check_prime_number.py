# Assign a value to num
num = 29
# Assume num is prime
is_prime = True
# Check for factors from 2 to num//2
for i in range(2, num // 2 + 1):
    if num % i == 0:
        is_prime = False
        break
# Print if num is prime or not
if is_prime:
    print("Prime")
else:
    print("Not Prime")
