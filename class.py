class Animal:
    def __init__(self, name):
        self.__name = name

    def sleep(self, *act):
        for key, value in enumerate(act):
            print(str(key) + ": " + value)
        print("Animal Sleep")


dog = Animal("Dog")

dog.__name = "cat"

print(dog._Animal__name)

dog.sleep("dance", "lol")

# inheritance


class Dog(Animal):
    def __init__(self, name):
        self.__name = name
        self.__type = "dogs"

    def type(self):
        print("This is " + self.__type)

    def sleep(self):
        print("Dog no sleeps")


dog = Dog("Kiki")

print(dog._Dog__name)

dog.type()
dog.sleep()
