import time
def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def tail_fibonacci(n: int, a: int = 0, b: int = 1) -> int:
    if n == 0:
        return a
    if n == 1:
        return b
    return tail_fibonacci(n - 1, b, a + b)

if __name__ == "__main__":
    n = 35
    
    start_time = time.time()
    print(f"Fibonacci({n}) = {fibonacci(n)}")
    print(f"Time taken (Naive): {time.time() - start_time:.6f} seconds")
    
    start_time = time.time()
    print(f"Tail Fibonacci({n}) = {tail_fibonacci(n)}")
    print(f"Time taken (Tail): {time.time() - start_time:.6f} seconds")
