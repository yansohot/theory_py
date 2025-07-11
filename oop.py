class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def move(self, new_x, new_y):
        self.x += new_x
        self.y += new_y

    def length(self, point):
        result = ((point.x - self.x) ** 2 + (point.y - self.y) ** 2) ** 0.5
        return round(result, 2)
    
class RedButton:
    def __init__(self) -> None:
        self.counter = 0

    def click(self):
        self.counter += 1
        print('Тревога!')

    def count(self):
        return self.counter
    
# simple

class Programmer:

    def __init__(self, name, position) -> None:
        rank = {
            'Junior': 10,
            'Middle': 15,
            'Senior': 20
        }
        self.name = name
        self.wage = rank[position]
        self.work_time = 0
        self.salary = 0

    def work(self, time):
        self.work_time += time
        self.salary += self.wage * time

    def info(self):
        return f'{self.name} {self.work_time}ч. {self.salary}тгр.'

    def rise(self):
        if self.wage < 20:
            self.wage += 5
        else:
            self.wage += 1

class Rectangle:
    def __init__(self, corner1, corner2) -> None:
        self.left_down = min(corner1[0], corner2[0]), min(corner1[1], corner2[1])
        self.up_right = max(corner1[0], corner2[0]), max(corner1[1], corner2[1])

    def perimeter(self):
        return round((self.up_right[0] - self.left_down[0]) * 2 +
                     (self.up_right[1] - self.left_down[1]) * 2, 2)

    def area(self):
        return round((self.up_right[0] - self.left_down[0]) *
                     (self.up_right[1] - self.left_down[1]), 2)
    
# продолжение первого, наивного решения

class Rectangle:
    def __init__(self, corner1, corner2) -> None:
        self.left_down = [min(corner1[0], corner2[0]),
                          min(corner1[1], corner2[1])]
        self.up_right = [max(corner1[0], corner2[0]),
                         max(corner1[1], corner2[1])]

    def perimeter(self):
        return round((self.up_right[0] - self.left_down[0]) * 2 +
                     (self.up_right[1] - self.left_down[1]) * 2, 2)

    def area(self):
        return round((self.up_right[0] - self.left_down[0]) *
                     (self.up_right[1] - self.left_down[1]), 2)

    def get_pos(self):
        return round(self.left_down[0], 2), round(self.up_right[1], 2)

    def get_size(self):
        return round(self.up_right[0] - self.left_down[0], 2), \
            round(self.up_right[1] - self.left_down[1], 2)

    def move(self, dx, dy):
        self.left_down[0] += dx
        self.left_down[1] += dy
        self.up_right[0] += dx
        self.up_right[1] += dy

    def resize(self, width, height):
        self.up_right[0] = self.left_down[0] + width
        self.left_down[1] = self.up_right[1] - height

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def move(self, new_x, new_y):
        self.x += new_x
        self.y += new_y

    def length(self, point):
        result = ((point.x - self.x) ** 2 + (point.y - self.y) ** 2) ** 0.5
        return round(result, 2)


class PatchedPoint(Point):
    def __init__(self, *args) -> None:
        match len(args):
            case 0:
                self.x = 0
                self.y = 0
            case 1:
                self.x, self.y = args[0]
            case 2:
                self.x, self.y = args

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def move(self, new_x, new_y):
        self.x += new_x
        self.y += new_y

    def length(self, point):
        result = ((point.x - self.x) ** 2 + (point.y - self.y) ** 2) ** 0.5
        return round(result, 2)


class PatchedPoint(Point):
    def __init__(self, *args) -> None:
        match len(args):
            case 0:
                self.x = 0
                self.y = 0
            case 1:
                self.x, self.y = args[0]
            case 2:
                self.x, self.y = args

    def __str__(self) -> str:
        string = f'({self.x}, {self.y})'
        return string

    def __repr__(self) -> str:
        string = f'PatchedPoint({self.x}, {self.y})'
        return string