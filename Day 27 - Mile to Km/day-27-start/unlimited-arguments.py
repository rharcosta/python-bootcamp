# unlimited arguments (inputs)
def add(*args):
    total = 0
    for n in args:
        total += n
    # print(total)


add(3, 4, 5, 6)


# unlimited keywords arguments
def calculate(n, **kwargs):
    # print(f"Dictionary: {kwargs}")
    # print(kwargs["add"]) -> the value of the 'add'
    n += kwargs["add"]  # 2 + 3
    n *= kwargs["multiply"]  # 5 * 5
    # print(n)  # N = 25


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")


car = Car(make="Nissan")
print(car.make)
print(car.model)  # model = none because of the .get


def bar(spam, eggs, toast='yes please!', ham=0):
    print(spam, eggs, toast, ham)


bar(1, 2)


def test(*args):
    print(args)


test(1, 2, 3, 5) # type = tuple


def all_aboard(a, *args, **kw):
    print(a, args, kw)


all_aboard(4, 7, 3, 0, x=10, y=64)
