# code

# Function to generate Fibonacci series up to n terms
def fibonacci(n):
    # Initialize Fibonacci series with first two terms
    fib_series = [0, 1]
    
    # Generate remaining terms until series length reaches n
    while len(fib_series) < n:
        # Calculate next term as sum of last two terms
        fib_series.append(fib_series[-1] + fib_series[-2])
    
    # Return generated Fibonacci series
    return fib_series

# Get class size from user input
class_size = int(input("Enter your class size: "))

# Generate Fibonacci series for class size
fib_series = fibonacci(class_size)

# Print Fibonacci series header
print("Fibonacci Series of your class members:")

# Print generated Fibonacci series
print(fib_series)