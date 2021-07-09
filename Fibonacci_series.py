def fib_series(n):
    i, j = 0, 1
    for count in range(n):
        nth_term = i + j
        i = j
        j = nth_term
        count += 1
        import sys
        sys.stdout.write(str(nth_term) + "\t")


fib_series(10)
