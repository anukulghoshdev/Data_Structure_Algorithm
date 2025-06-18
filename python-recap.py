"""
name = str(input("Your name: "))
age = int(input("Your age: "))
color = input("Your fav. color: ")
subject = input("Your subject: ")
city = input("Your city: ")
print(f"My name is {name}. I'm {age} years old.I study {subject} and I live in {city}")
"""

"""
number = int(input("Enter a number: "))
if number%2== 0: 
    print("Even")
else: 
    print("Odd")
"""

"""
names = []

for i in range(5):
    name = input(f"Enter name {i+1}: ")
    names.append(name)

print("\nThe names you entered are: ")
for name in names: 
    print(name)
"""

"""
n = 1
while n<=5: 
    if n == 3:
        n+=1
        continue
    print(n)
    n+=1
"""

"""
password = ""
correct_password = "1234"
while password != correct_password:
    password = input("Enter the password: ")
    if password != "1234":
        print("Incorrect password! Try again.") 
print("access granted!")    
"""

age = int(input("Enter your age: "))
if age<=12:
    print("You are a child")
elif age<=17:
    print("You are a teenager.")
elif age<=59:
    print("You are an adult.")
else: 
    print("You are a senior citizen.")














