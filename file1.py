# file1.py
def factorial(n):
if n == 0:
    return 1
else:
    return n * factorial(n-1)

result = factorial(5)
print("Factorial of 5 is: {result}")

def fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
             return sequence

result = fibonacci_sequence(10)
print("Fibonacci sequence up to 10 numbers: {result}") 

# file1.py
def newfactorial(n):
if n == 0:
    return 1
else:
    return n * factorial(n-1)

result = factorial(5)
print("Factorial of 5 is: {result}")
