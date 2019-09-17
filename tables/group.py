class Group:
    def __init__(self):
        self.count = 0
        self.names = []

    def add_people(self, people):
        name, count = people
        self.count += count
        self.names.append(name)

    def display(self):
        for name in self.names:
            print(name)
