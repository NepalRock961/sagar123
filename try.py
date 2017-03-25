def fib(n):
    a, b = 0, 1

    while a < n:
        print(a)
        (a, b) = (b, a + b)


def main():
    n = int(input('N = '))

    # Print the series upto n
    print (fib(n))

# Now this is what triggers everything
# when the program starts.
main()