my_list = [10, 20, 30, 40]
print(my_list[0])
my_list[0] = 33
my_list.append(55)
my_list.insert(1,50)
print(my_list)
my_list.pop()
print(my_list)
del my_list[1]
print(my_list)
print(len(my_list))

# access with loop 
for item in my_list: 
    print(item)

for i in range(len(my_list)):
    print(my_list[i])

# practice problem 1
# 5টি নাম ইনপুট নিয়ে একটি লিস্টে রাখো এবং সবগুলো প্রিন্ট করো (loop দিয়ে)
names = []
for i in range(5):
    nam = input(f"Enter your name {i+1}: ")
    # if (nam == ''):
    #     print("please write a name ")
    #     nam = input(f"Enter your name {i+1}: ")

    while nam.strip() == '':  # strip() দিয়ে স্পেস-only ইনপুটও ধরা যাবে
        print("Please write a name!")
        nam = input(f"Enter your name {i+1}: ")

    names.append(nam)

for name in names:
    print(f"{name}")
print(names)


# type2 practice problem 1:
names = []
while True:
    name = input("Enter your name (or type 'exit' to shop): ").strip()
    if name.lower() == "exit":
        break
    if name == '':
        print("Please write a valid name!")
        continue
    if name in names: 
        print(f"{name} is already in the list! Please enter a different name.")
        continue
    names.append(name)
print(f"final names in the list: {names}")
for i in names: 
    print(f"{i}", end=", ")


# practice problem 2
numbers = []
i=0
while i<5:
    number = int(input("Enter the numbers: "))
    if type(number) != int:
        print("Please Enter a valid Number") 
        continue
    numbers.append(number)
    i+=1
for n in numbers:
    print(f"{n}", end=" ")


# practice problem 2: type2
numbers = []
i = 0
while i < 5:
    number = input("Enter the numbers: ")
    if not number.isdigit():   # check number string কিনা
        print("Please Enter a valid Number")
        continue
    numbers.append(int(number))  # এখন convert করলে কোনো error হবে না
    i += 1

for n in numbers:
    print(f"{n}", end=" ")


# practice problem 2: type 3
numbers = []  
i = 0  

while i < 5:  
    try:  
        number = int(input("Enter the number: "))  # input কে int এ convert করা হচ্ছে  
        numbers.append(number)  
        i += 1  
    except ValueError:  
        print("Please enter a valid number!")  

print("The numbers are: ", end=" ")  
for n in numbers:  
    print(n, end=" ")  



