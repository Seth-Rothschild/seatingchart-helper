class Table:
    def __init__(self, name="", capacity=12):
        self.count = 0
        self.name = name
        self.groupslist = []
        self.capacity = capacity
        self._update_remaining()

    def add_group(self, group):
        if group.count <= self.remaining:
            self.count += group.count
            self.groupslist.append(group)
            self._update_remaining()

    def remove_group(self, group):
        if group in self.groupslist:
            self.groupslist.remove(group)
            self.count -= group.count
            self._update_remaining()

    def display(self):
        if self.name != "":
            tblname = "{} ({})".format(self.name, self.count)
            print("-" * (len(tblname) + 2))
            print(tblname)
            print("-" * (len(tblname) + 2))
        for group in self.groupslist:
            print(group.display())
        print("")

    def _update_remaining(self):
        self.remaining = self.capacity - self.count

    def set_name(self, name):
        self.name = name
