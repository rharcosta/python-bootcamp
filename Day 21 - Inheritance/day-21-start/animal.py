# class inheritance
class Animal:
    def __init__(self):
        self.eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


# class Fish is referring to the class Animal
class Fish(Animal):
    def __init__(self):
        # the call to super() is recommended, but not strictly required
        super().__init__()

    def breathe(self):
        super().breathe()
        print("Doing this underwater.")

    def swim(self):
        print("Moving in water.")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.eyes)
