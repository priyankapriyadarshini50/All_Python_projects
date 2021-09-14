class Dog:
    color = 'white'

    def __init__(self, name):
        self.name = name
        # self.color = 'black' # here color is an instance variable

    def speak(self):
        return self.name + ' says woof!' + 'and Color is ' + self.color  # self keyword can access the class variable


class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says meow!'


tommy = Dog('Tommy')
katty = Cat('Katty')

print(tommy.speak())
print(katty.speak())

print(tommy.color)
print(tommy.__dict__)
print(Dog.__dict__)
print()

for pet in [tommy, katty]:
    print(type(pet))
    print(pet.speak())
# another way:
def pet_speak(pet1):
    print(pet1.speak())


pet_speak(tommy)
pet_speak(katty)

