class Zoo(object):
    def __init__(self):
        self._animals = {}
        self._id_count = 0

    def add(self, animal):
        id = self._id_count
        animal.id = id
        self._id_count += 1
        self._animals[id] = animal

    def get(self, id):
        return self._animals.get(id)

    def get_range(self, start, amount):
        return [self.get(id) for id in range(start, start + amount)]

    def get_all(self):
        return self._animals.values()


class Animal(object):
    def __init__(self, name, species):
        self.name = name
        self.species = species

zoo = Zoo()

zoo.add(Animal('Bob', 'snake'))
zoo.add(Animal('Anna', 'snake'))
zoo.add(Animal('Fred', 'elephant'))
zoo.add(Animal('Kate', 'tiger'))
