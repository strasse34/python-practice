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


 
def save_data(**user):
    print(user)


save_data(id=1, fname='reza', lname='mirzaie', age=40)

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

users_dic = {}
for user in users:
    key = user[0]
    value = user[1]
    users_dic[key] = value
print(users_dic)
