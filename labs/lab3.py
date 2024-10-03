import time

# Naive approach
def fibonacci_naive(n):
    if n <= 1:
        return n
    return fibonacci_naive(n-1) + fibonacci_naive(n-2)

# Memoization approach
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
        return n
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]

# Measure time for naive approach
start_time_naive = time.time()
naive_result = fibonacci_naive(40)
time_naive = time.time() - start_time_naive

# Measure time for memoization approach
start_time_memo = time.time()
memo_result = fibonacci_memo(40)
time_memo = time.time() - start_time_memo

# Print results and time taken
print(f"Naive Fibonacci result for F(40): {naive_result}, Time taken: {time_naive:.4f} seconds")
print(f"Memoized Fibonacci result for F(40): {memo_result}, Time taken: {time_memo:.6f} seconds")
