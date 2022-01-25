def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


try:
    f = factorial(990)
    print(f)
except (RecursionError, ZeroDivisionError):
    print("This program can not calculate factorial that large")

print("Program terminating")
