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

# sum of 1 to n
def  sum_n(n):
    if n == 1:
        return 1
    else: 
        return n + sum_n(n-1)

print(sum_n(5))

#fibonacci seris using recursion
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(5))
    
# assignment 3
def is_even_recursive(n):
    if n == 0:
        return True
    elif n == 1:
        return False
    else: 
        return is_even_recursive(n-2)
print(is_even_recursive(6))
print(is_even_recursive(9))

