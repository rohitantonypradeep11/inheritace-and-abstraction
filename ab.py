from abc import ABC,abstractmethod
class animal(ABC):
    def move(self):
        pass
class human(animal):
    def move(self):
        print("i can run")
class snake(animal):
    def move(self):
        print("i can crawl")
class dog(animal):
    def move(self):
        print("i can bark")
r  = human()
r.move()
a = snake()
a.move()
b = dog()
b.move()