# 아래 클래스를 수정하시오.
class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        self.area = self.width * self.height
        return self.area
    
    def calculate_perimeter(self):
        self.perimeter = (2*self.width) + (2*self.height)
        return self.perimeter


shape1 = Shape(5, 3)
perimeter1 = shape1.calculate_perimeter()
print(perimeter1)
