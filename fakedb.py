class Zoo(object):
    def __init__(self):
        self._animals = {}
        self._id_count = 0

    def add(self, animal):
        id = self._id_count
        animal.id = id
        self._id_count += 1
        self._animals[id] = animal

    def remove(self, id):
        del self._animals[id]

    def total(self):
        return len(self._animals)

    def get(self, id):
        return self._animals.get(id)

    def get_range(self, start, amount):
        result = []
        for id in range(start, start + amount):
            animal = self.get(id)
            if animal is None:
                break
            result.append(animal)
        return result

    def get_all(self):
        return self._animals.values()


class Animal(object):
    def __init__(self, name, species):
        self.name = name
        self.species = species


class Mammal(Animal):
    pass


zoo = Zoo()

zoo.add(Animal('Bob', 'snake'))
zoo.add(Animal('Fred', 'snake'))
zoo.add(Mammal('Anna', 'elephant'))
zoo.add(Mammal('Kate', 'tiger'))

