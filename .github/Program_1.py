

class triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def sides_total(self):
        perimeter = self.a + self.b + self.c
        return perimeter

t1 = triangle(3, 4, 5)
perimeter = t1.sides_total()
print(f'The perimeter of the triangle is {perimeter}')