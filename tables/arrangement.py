import csv
from tables.table import Table
from tables.group import Group


class Arrangement:
    def __init__(self, csv_path=""):
        self.tables = []
        self.unseated = []
        self.raw = []
        if csv_path != "":
            self.read_csv(csv_path)

    def export(self, csv_path):
        with open(csv_path, mode="w") as csvfile:
            writeCSV = csv.writer(csvfile, delimiter=",")
            for table in self.tables:
                for group in table.groupslist:
                    for people in group.people:
                        name, count = people
                        writeCSV.writerow([name, count, group.name, table.name])
            for group in self.unseated:
                for people in group.people:
                    name, count = people
                    if name != group.name:
                        writeCSV.writerow([name, count, group.name, ""])
                    else:
                        writeCSV.writerow([name, count, "", ""])

    def read_csv(self, csv_path):
        with open(csv_path) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=",")
            for row in readCSV:
                self.raw.append(row)
        self._create_groups_from_raw()
        self._create_tables_from_raw()
        self._assign_assigned()

    def add(self, group_name, table_name):
        table = self._find_table(table_name)
        groups_to_remove = []
        for i, group in enumerate(self.unseated):
            if group.name == group_name:
                table.add_group(group)
                groups_to_remove.append(group)
        for group in groups_to_remove:
            self.unseated.remove(group)

    def remove(self, group_name, table_name):
        table = self._find_table(table_name)
        groups_to_remove = []
        for group in table.groupslist:
            if group.name == group_name:
                self.unseated.append(group)
                groups_to_remove.append(group)
        for group in groups_to_remove:
            table.groupslist.remove(group)

    def display(self):
        for table in self.tables:
            table.display()
        print("Unseated")
        for group in self.unseated:
            group.display()

    def _assign_assigned(self):
        for row in self.raw:
            _, _, gname, tname = row
            if tname != "":
                self.add(gname, tname)

    def _find_table(self, table_name):
        return list(filter(lambda tab: tab.name == table_name, self.tables))[0]

    def _find_unseated_group(self, group_name):
        return list(filter(lambda grp: grp.name == group_name, self.unseated))[0]

    def _create_default_tables(self):
        self.tables = [Table(name="sweetheart", capacity=2)]
        self.tables += [Table(name="table {}".format(i)) for i in range(1, 16)]

    def _create_groups_from_raw(self):
        group_names = list(set([row[2] for row in self.raw]))
        if "" in group_names:
            group_names.remove("")

        for name in group_names:
            self.unseated.append(Group(name=name))

        for row in self.raw:
            name, count, group_name, table_name = row
            people = (name, int(count))
            if group_name in group_names:
                self._find_unseated_group(group_name).add_people(people)
            else:
                gr = Group(name=name)
                gr.add_people(people)
                self.unseated.append(gr)

    def _create_tables_from_raw(self):
        table_names = list(set([row[3] for row in self.raw]))
        if "" in table_names:
            table_names.remove("")
        for name in table_names:
            self.tables.append(Table(name=name))
