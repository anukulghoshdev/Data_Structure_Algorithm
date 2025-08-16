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