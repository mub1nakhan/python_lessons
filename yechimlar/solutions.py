class Dog:
    def __init__(self, name: str, age: int,color: str, owner: str):
        self.name = name
        self.age = age
        self.color = color
        self.owner = owner

    def yap(self):
        print("wow wow")


  #method

    def move (self, speed = 12, time: float = 1.1):
        self.yap()
        return speed * time

Clara = Dog("Clara", 2, "blonde", "Tom")

print(Clara.move(14, 2.3))
