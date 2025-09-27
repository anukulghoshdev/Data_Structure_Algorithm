# List items are ordered, changeable, and allow duplicate values.
# store multiple items in a single variable.

# list methods: append(), insert(), pop(), remove(), clear(), sort(), reverse(), count(), index(), extend()
my_list = [10, 20, 30, 40]
print(my_list[0])

my_list[0] = 33
my_list.append(55)

my_list.insert(1,50) # index, value
print(my_list)

my_list.pop() # default last item remove
print(my_list)

my_list.remove(30)
print(my_list)

my_list.pop(2)
print(my_list)

del my_list[1]
print(my_list)

my_list.clear() # empty list 
print(my_list)

print(len(my_list))

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist) # ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist) # ['apple', 'banana', 'cherry', 'kiwi', 'orange']

# access with loop 
for item in my_list: 
    print(item)

for i in range(len(my_list)):
    print(my_list[i])

# practice problem 1 type 1
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


# practice problem 1 type2:
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


# practice problem 2 type 1
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

# practice problem 3: type 1:
numbers = []  

n = int(input("How many numbers do you want to enter? "))

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("Your numbers are:", numbers)



# practice problem 3: type 2:
numbers = []  

n = int(input("How many numbers do you want to enter? "))

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
print("Your numbers are:", numbers)

# sum = 0
# for number in numbers:
#     sum += number
# print("Sum is :", sum)

sum = sum(numbers)
print("Sum is :", sum)
average = sum / n
print("Average is :", average)

max_num = max(numbers)
min_num = min(numbers)
print("Maximum number is :", max_num)
print("Minimum number is :", min_num) 

# problem 4
my_list = [13, 22, 33, 46, 51, 60, 77, 88, 95]

#  list comprehensions:
even_numbers = [item for item in my_list if item % 2 == 0]
odd_numbers = [item for item in my_list if item % 2 != 0]
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

# tuple Unpacking ট্রিক:
even_numbers, odd_numbers = (
    [item for item in my_list if item % 2 == 0],
    [item for item in my_list if item % 2 != 0]
)

# Dictionary comprehension:
number = {
    "even" : [item for item in my_list if item % 2 == 0],
    "odd" : [item for item in my_list if item % 2 != 0]
}
even_numbers = number["even"]
odd_numbers = number["odd"]

print ("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)


# set comprehension
my_list = [13, 22, 33, 46, 51, 60, 77, 88, 95]

even_numbers = {item for item in my_list if item % 2 == 0}
odd_numbers = {item for item in my_list if item % 2 != 0}

print("Even numbers (set):", even_numbers)
print("Odd numbers (set):", odd_numbers)

# normal way:
for item in my_list:
    if item % 2 == 0:
        even_numbers.append(item)
    else:
        odd_numbers.push(item)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

# problem 5: reverse a list

num_elements = int(input("How many elements do you want to add in the list? ")) 
my_list = []
for i in range(num_elements):
        element = input(f"Enter element {i+1}: ")
        my_list.append(element)
print(f"Your list is: {my_list}")
my_list.reverse() # my_list[::-1]
print(f"Reversed list is: {my_list}")
