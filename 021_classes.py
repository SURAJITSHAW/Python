class Point:

    def __init__(self, x, y):
        self.x_axis = x
        self.y_axis = y

    def move(self):
        print('Move...')
    
    def draw(self):
        print('Draw.')


point1 = Point(1, 2)
print(point1.x_axis)