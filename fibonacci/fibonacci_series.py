# Number of terms in the Fibonacci series
num_terms = 10

# Initialize the first two terms of the Fibonacci series
t1, t2 = 0, 1

# Print the first two terms
print("Fibonacci Series:", t1, t2, end=" ")

# Loop to calculate the rest of the terms
for _ in range(2, num_terms):  
    next_term = t1 + t2  
    print(next_term, end=" ")  
    t1, t2 = t2, next_term  
