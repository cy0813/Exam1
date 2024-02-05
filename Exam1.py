# -*- coding: utf-8 -*-
class Geometric():
    def __init__(self):                  #建構函數(初始化)
        self.color = "Green"
class Circle(Geometric):
    def __init__(self,radius):           #self的定義是為了變成全域變數
        super().__init__()               #可以讓子類別繼承父類別的__init__功能
        self.PI = 3.14159
        self.radius = radius
    def getRadius(self):                 #沒有self的函數為區域變數，所以不能沒有self
        return self.radius
    def setRadius(self,radius):
        self.radius = radius
    def getDiameter(self):
        return self.radius * 2
    def getPerimeter(self):
        return self.radius * 2 * self.PI
    def getArea(self):
        return self.PI * (self.radius ** 2)


test = Circle(5)

print("圓形的半徑 : ", test.getRadius())
print("圓形的直徑 : ", test.getDiameter())
print("圓形的圓周 : ", test.getPerimeter())
print("圓形的面積 : ", test.getArea())
test.setRadius(10)
print("圓形的直徑 : ", test.getDiameter())