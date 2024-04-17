class Person:
    next_id = 0

    def __init__(self, name):
        self.name = name
        self.id = Person.next_id
        Person.next_id += 1

    def __lt__(self, other):
        return self.id < other.id

    def __gt__(self, other):
        return self.id > other.id

    def __eq__(self, other):
        return self.id == other.id

    def __le__(self, other):
        return self.id <= other.id

    def __ge__(self, other):
        return self.id >= other.id