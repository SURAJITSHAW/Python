class Mammal:
    def walk(self):
        print('Walking...')


class Dog(Mammal):
    def barking(self):
        print('bark! bark!')


tommy = Dog()
tommy.walk()
tommy.barking()