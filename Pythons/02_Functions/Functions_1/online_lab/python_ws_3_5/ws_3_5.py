number_of_people = 0
number_of_book = 100

def increase_user():
    pass


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

def decrease_book(number):
    global number_of_book
    number_of_book -= number
    print(f'남은 책의 수 : {number_of_book}')
    return number_of_book


def create_user(name, age ,address):
    increase_user()
    user_info = {}
    user_info['name'] = name
    user_info['age'] = age
    user_info['address'] = address
    result = user_info
    print(f'{name}님 환영합니다!')
    return result

many_user = list(map(create_user, name, age, address))

def rental_book(info):
    number = info['age'] // 10
    decrease_book(number)
    print(f'{info["name"]}님이 {number}권의 책을 대여하였습니다.')

# print(many_user)
info = list(map(lambda x:{'name':x['name'], 'age' : x['age']}, many_user))
list(map(rental_book,info))

