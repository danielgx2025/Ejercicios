def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        # Genera la serie hasta n-1 y añade el siguiente número
        prev_fib = fibonacci(n - 1)
        prev_fib.append(prev_fib[-1] + prev_fib[-2])
        return prev_fib

# Ejemplos de uso:
#print(f"Fibonacci(0): {fibonacci(0)}")
#print(f"Fibonacci(1): {fibonacci(1)}")
#print(f"Fibonacci(2): {fibonacci(2)}")
print(f"Fibonacci(5): {fibonacci(5)}")
#print(f"Fibonacci(10): {fibonacci(10)}")
