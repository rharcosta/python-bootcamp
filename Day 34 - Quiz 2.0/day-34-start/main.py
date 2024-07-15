# type hints

# I'm defining name as a string and the function will also return a string
def greeting(name: str) -> str:
    return "Hello " + name


value = greeting("Rubia")
print(value)
