def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    print(memo)
    return memo[n]

print(fib_memo(3))
print(fib_memo(3))
