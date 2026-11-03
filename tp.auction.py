class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return "..."

    def describe(self):
        return f"{self.name} says {self.sound()}"

class Dog(Animal):
    def __init__(self, name):
            self.name = name
    def sound(self):
        return "Woof"

class Cat(Animal):
    def __init__(self, name):
            self.name = name
    def sound(self):
        return "Meow"


# pour tester

try:
    assert Dog("Rex").describe() == "Rex says Woof"
    assert Cat("Tom").describe() == "Tom says Meow"
    assert Animal("Ghost").describe() == "Ghost says ..."
    assert isinstance(Dog("Rex"), Animal)
    assert issubclass(Cat, Animal)
    assert "describe" not in vars(Dog), "describe must be inherited, not rewritten"
except Exception as e:
    print("OOPS - Something's wrong")
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works !')

