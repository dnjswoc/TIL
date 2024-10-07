class Animal:
    num_of_animal = 0
    def __init__(self):
        Animal.num_of_animal += 1


class Dog(Animal):
    sound = '멍멍'
    def __init__(self):
        super().__init__()


    def bark(self):
        print('멍멍!')


class Cat(Animal):
    sound = '야옹'
    def __init__(self):
        super().__init__()
    

    def meow(self):
        print('야옹!')

class Pet(Cat, Dog):
    def __init__(self):
        super().__init__()
        

    @classmethod
    def access_num_of_animal(cls):
        return f'동물의 수는 {cls.num_of_animal}마리 입니다.'
    
    def play(self):
        print('애완동물과 놀기')
    
    def make_sound(self):
        print(self.sound)
    
    def __str__(self):
        return f'애완동물은 {super().sound} 소리를 냅니다.'
    
pet1 = Pet()
print(pet1)