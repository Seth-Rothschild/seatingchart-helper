class Group:
    def __init__(self):
        self.count = 0
        self.names = []
        self.countlist = []
        self.name = ""

    def add_people(self, people):
        name, count = people
        self.count += count
        self.names.append(name)
        self.countlist.append(count)

    def display(self):
        for name in self.names:
            print(name)

    def set_name(self, name):
        self.name = name
