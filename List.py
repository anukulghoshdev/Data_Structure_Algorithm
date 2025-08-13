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
