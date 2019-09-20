import csv


class TableList:
    def __init__(self, csv_path=""):
        self.tables = []
        self.groups = []
        self.raw = []
        if csv_path != "":
            self.read_csv(csv_path)

    def export(self):
        for table in self.tables:
            table.display()

    def read_csv(self, csv_path):
        with open(csv_path) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=",")
            for row in readCSV:
                self.raw.append(row)

    def add(self, group_name, table_name):
        table = list(filter(lambda tab: tab.name == table_name, self.tables))[0]
        for i, group in enumerate(self.groups):
            if group.name == group_name:
                table.add_group(group)
                self.groups.pop(i)

    def remove(self, group_name, table_name):
        table = list(filter(lambda tab: tab.name == table_name, self.tables))[0]
        groups_to_remove = []
        for group in table.groupslist:
            if group.name == group_name:
                self.groups.append(group)
                groups_to_remove.append(group)
        for group in groups_to_remove:
            table.groupslist.remove(group)
