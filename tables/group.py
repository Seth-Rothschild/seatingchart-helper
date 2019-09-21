class Group:
    def __init__(self, name=""):
        self.count = 0
        self.people = []
        self.name = name

    def add_people(self, people):
        _, count = people
        self.count += count
        self.people.append(people)

    def display(self):
        for name, count in self.people:
            print(name)

    def set_name(self, name):
        self.name = name
