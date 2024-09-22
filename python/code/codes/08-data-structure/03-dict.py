# clear
person = {'name': 'Alice', 'age': 25}
person.clear()
print(person)

# get
person = {'name': 'Alice', 'age': 25}
print(person.get('name'))
print(person.get('country'))
print(person.get('country', 'Unknown'))
# print(person['country'])  # KeyError: 'country'

# keys
person = {'name': 'Alice', 'age': 25}
print(person.keys())  # dict_keys(['name', 'age'])
for item in person.keys():
    print(item)

# values
person = {'name': 'Alice', 'age': 25}
print(person.values())  # dict_values(['Alice', 25])
for item in person.values():
    print(item)

# items
person = {'name': 'Alice', 'age': 25}
print(person.items())  # dict_items([('name', 'Alice'), ('age', 25)])
for key, value in person.items():
    print(key)
    print(value)

# pop
person = {'name': 'Alice', 'age': 25}
print(person.pop('age'))  # 25
print(person)  # {'name': 'Alice'}
print(person.pop('country', None))  # None
# print(person.pop('country'))  # KeyError: 'country'


# setdefault
person = {'name': 'Alice', 'age': 25}
print(person.setdefault('country', 'KOREA'))  # KOREA
print(person)  # {'name': 'Alice', 'age': 25, 'country': 'KOREA'}


# update
person = {'name': 'Alice', 'age': 25}
other_person = {'name': 'Jane', 'gender': 'Female'}

person.update(other_person)
print(person)  # {'name': 'Jane', 'age': 25, 'gender': 'Female'}

person.update(age=100, country='KOREA')
print(person)  # {'name': 'Jane', 'age': 100, 'gender': 'Female', 'country': 'KOREA'}

# a = {}
# b = {'name': 'Alice', 'age': 25}

# a.update(b)
# print(a)  # {'name': 'Alice', 'age': 25}
# b['name'] = 'Harry'
# print(a)  # {'name': 'Alice', 'age': 25}
