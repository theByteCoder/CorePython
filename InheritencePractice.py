class Animal:
    def legs(self, animal_name, num_of_legs):
        print(f'The animal {animal_name} has {num_of_legs} number of legs')


class Dogs(Animal):
    pass


class Cats(Animal):
    pass


dogs = Dogs()
dogs.legs('Dog', 4)

cats = Cats()
cats.legs('Cat', 4)
