class Person:
    # 클래스 변수 count
    count = 0

    def __init__(self, name):
        # 인스턴스 변수 name
        self.name = name
        Person.count += 1

person1 = Person('iu')
person2 = Person('BTS')

print(Person.count)  # 2

##########################

class Circle:
    pi = 3.14

    def __init__(self, r):
        self.r = r

c1 = Circle(5)
c2 = Circle(10)

print(c1.r)
print(c2.r)

# c1의 인스턴스 변수 pi를 생성
c1.pi = 100

print(Circle.pi)  # 3.14
print(c1.pi)  # 100
print(c2.pi)  # 3.14



