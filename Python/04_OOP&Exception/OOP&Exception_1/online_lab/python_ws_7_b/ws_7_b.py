# 아래에 코드를 작성하시오.
class Myth:
    type_of_myth = 0

    def __init__(self, name):
        self.name = name
        Myth.type_of_myth+=1
    
    def __str__(self):
        return self.name

    @staticmethod
    def Myth_description():
        print('신화는 한 나라 혹은 한 민족으로부터 전승되어 오는 예로부터 섬기는 신을 둘러싼 이야기를 뜻한다.')

Myth_1 = Myth('dangun')
Myth_2 = Myth('greek & rome')
print(Myth_1)
print(Myth_2)
print(Myth.type_of_myth)
Myth.Myth_description()