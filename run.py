x = 1
while x < 5:
    print(x)
    x +=1

for num, char in enumerate('python', start=1):
    print(f'{num}- {char.upper()}')
    if char == 'o':
        print(f'One "o" was found!'.upper())
        pass

for char in 'python':
    print([char])

   
def greet(first_name, last_name, age):
    print(f'{first_name} {last_name}: {age} years old.')


message = greet('reza', 'mirzaie', 40)
print(message)

print()
print('**functionality ...................................')
def save_data(**user):
    print(user)


save_data(id=1, fname='reza', lname='mirzaie', age=40)

print()
print('distracting itmes from a list or tuple ................')
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

print()
print('using map(), filter, and lambda .....................')
name = list(map(lambda user: user[0], users))
age = list(map(lambda user: user[1], users))
filtered = list(filter(lambda user: user[1] < 30, users))
print(name , age, filtered)

print()
print('or comperhention .................................')
name = [user[0] for user in users]
age = [user[1] for user in users]
filtered = [user[1] for user in users if user[1] < 30]

print(name , age, filtered)

print()
print('changing a list to dic ...................................')
users_dic = {}
for user in users:
    key = user[0]
    value = user[1]
    users_dic[key] = value
print(users_dic)


print(dict(users))

print(list(users_dic))

print()
print('items() method ...................................')
print(list(users_dic.items()))

for x in users_dic.items():
    print(x)
print()
print('khali kardan baar-e yek list ba *........................')
print(*users)

ali = users[0]

print(ali)
print(*ali)

print()
print('khali kardan baar yek dict ba **..........................')
first = {'ali': 20, 'moha': 40, 'hasti': 23}
second = {'fname': 'reza', 'lname': 'mirzaie'}
print({**first, 'age': 40, **second})

print()
print('try, exception, else ...............................')

# try:
#     age = int(input('How old are you? '))
#     xfactor = 10/age
# except ValueError:
#     print('Please enter correct value!')
# except ZeroDivisionError:
#     print('you cant enter 0!')
# else:
#     print(f'Your age is {age}.')

# or

print()
print('rasie ...........................................')


def cal():
    num1 = int(input('numer 1: '))
    if num1 == 0:
        raise ValueError('Invalid Value!')        
    num2 = int(input('numer 2: '))
    if num2 == 0:
        raise ValueError('Invalid Value!')
    mult = num1 * num2
    print(mult)


try:
    cal()
except ValueError as v:
    print(v)
else:
    print('done!')

print()
print('classes ..............................................')


class Arusak:
    sex = 'female'
    vazn = 100

    def __init__(self, rng_chshm, rng_pust, rng_moo):
        self.rng_chshm = rng_chshm
        self.rng_pust = rng_pust
        self.rng_moo = rng_moo
    
    
    def good_quality(self):
        print(f'It is a high quality product, with a {self.rng_chshm} eyes, {self.rng_pust} skin and beatuful {self.rng_moo} hear')

    def medium_quality(self):
        print(f'It is a medum quality product with a {self.rng_chshm} eyes, {self.rng_pust} skin and beatuful {self.rng_moo} hear')

    def low_quality(self):
        print(f'It is a low quality product with a {self.rng_chshm} eyes, {self.rng_pust} skin and beatuful {self.rng_moo} hear')


african_arusak = Arusak('Black', 'Brown', 'black')
asian_arusak = Arusak('Brown', 'Yellow', 'Brwon')
eurupian_arusak = Arusak('Blue', 'white', 'yellow')

african_arusak.medium_quality()
print(african_arusak.sex, african_arusak.vazn)
eurupian_arusak.low_quality()
print(eurupian_arusak.sex, eurupian_arusak.vazn)
