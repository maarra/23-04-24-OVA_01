class Pet:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound


    def sound(self):
        print(f'Sound of this pet is {self.sound}')

    def show(self):
        print(f'Name of the pet is {self.name}')

    def type(self):
        pass

class Dog(Pet):
    _count = 0

    def __init__(self, name, sound, subspecies):
        super().__init__(name, sound)
        self.subspecies = subspecies
        Dog._count += 1

    @staticmethod
    def get_count():
        return Dog._count



dog1 =  Dog('Rex', 'Barkling', 'German Sheppard')
dog1.show()
dog1.sound()

class Cat(Pet):
    pass



class Parrot(Pet):
    pass



class Hamster(Pet):
    pass
