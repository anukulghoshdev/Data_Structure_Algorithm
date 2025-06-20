def countdown(n):
    if n == 0:
        print("Blast off")
    else:
        # print(n)
        countdown(n-1)

countdown(5)

# factorial(n) = n * factorial(n-1)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else: 
        return n * factorial(n-1)

print(factorial(5))
