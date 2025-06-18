# recursion in loop
# prev2 = 0
# prev1 = 1
# # print(prev2);
# for fibo in range(18):
#     newFibo = prev1+prev2
#     # print(newFibo)
#     prev2 = prev1
#     prev1 = newFibo
    # 0 1 1 2 3 5 8

# recursion in fuction call itself 
print(0)
print(1)
count = 2
def fibonacci(prev1,prev2):
    global count
    if count <= 19:
        newFibo = prev1 + prev2
        print(newFibo)
        prev2 = prev1
        prev1 = newFibo
        count+=1
        fibonacci(prev1, prev2)
    else:
        return
fibonacci(0,1)




# F(n) = F(n-1) + F(n-2)
def F(n):
    if n <= 1:
        return n
    else:
        return F(n-1) + F(n-2)
        
print(F(5))
# 0 1 1 2 3 5 8......