x = 1
while x < 5:
    print(x)
    x +=1

for num, char in enumerate('python', start=1):
    print(f'{num}- {char.upper()}')
    if char == 'o':
        print(f'One "o" was found!'.upper())
        pass


   
def greet(first_name, last_name, age):
    print(f'{first_name} {last_name}: {age} years old.')


message = greet('reza', 'mirzaie', 40)
print(message)


# ** functionality 
def save_data(**user):
    print(user)


save_data(id=1, fname='reza', lname='mirzaie', age=40)


#distracting itmes from a list or tuple
users = [
    ['ali', 20],
    ['moha', 40],
    ['hasti', 23]
]

name = []
age = []

for user in users:
    name.append(user[0])
    age.append(user[1])
print(name)
print(age)


# using map(), filter, and lambda
name = list(map(lambda user: user[0], users))
age = list(map(lambda user: user[1], users))
filtered = list(filter(lambda user: user[1] < 30, users))
print(name , age, filtered)
# or comperhention
name = [user[0] for user in users]
age = [user[1] for user in users]
filtered = [user[1] for user in users if user[1] < 30]

print(name , age, filtered)


# changing a list to dic
users_dic = {}
for user in users:
    key = user[0]
    value = user[1]
    users_dic[key] = value
print(users_dic)


print(dict(users))

print(list(users_dic))

print(list(users_dic.items()))

for x in users_dic.items():
    print(x)
