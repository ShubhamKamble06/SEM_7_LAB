# fibonacci with using recursion

def rec_fibo(n):
    if n <= 1:
        return n
    else:
        return (rec_fibo(n - 1) + rec_fibo(n - 2))

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    fib_sequence = [0, 1]
    for i in range(2, n + 1):
        next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_fib)

    return fib_sequence[n], len(fib_sequence) - 1

nterm = int(input("\n Enter no. of integers you wanted to print : "))

if nterm <= 0:
    print("Enter a positive integer.")
else:
    print("Fibonacci Series using Recursion:")
    for i in range(nterm):
        print(rec_fibo(i), end=" ")

n = int(input("\n Enter the fibonacci number you want to check : "))
fib_number, step_count = fibonacci(n)
print(f"fibonacci({n}) = {fib_number}")
print(f"number of steps : {step_count}")