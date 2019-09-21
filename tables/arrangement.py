import csv
from tables.table import Table
from tables.group import Group


class Arrangement:
    def __init__(self, csv_path=""):
        self._clear_arr()
        if csv_path != "":
            self.read_csv(csv_path)

    def _clear_arr(self):
        self.tables = []
        self.unseated = []
        self.raw = []

    def export(self, csv_path):
        with open(csv_path, mode="w") as csvfile:
            writeCSV = csv.writer(csvfile, delimiter=",")
            for table in self.tables:
                for group in table.groups:
                    for people in group.people:
                        name, count = people
                        row = [name, count, group.name, table.name]
                        writeCSV.writerow(row)
            for group in self.unseated:
                for people in group.people:
                    name, count = people
                    if name != group.name:
                        writeCSV.writerow([name, count, group.name, ""])
                    else:
                        writeCSV.writerow([name, count, "", ""])

    def read_csv(self, csv_path):
        self._clear_arr()
        with open(csv_path) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=",")
            for row in readCSV:
                self.raw.append(row)
        self._create_groups_from_raw()
        self._create_tables_from_raw()
        self._assign_assigned()

    def add(self, group_name, table_name):
        try:
            table = self._find_table(table_name)
            group = self._find_unseated_group(group_name)
            table.add_group(group)
            self.unseated.remove(group)
        except IndexError:
            print("Failed to add {} to {}".format(group_name, table_name))

    def remove(self, group_name):
        group, table = self._find_seated_group(group_name)
        self.unseated.append(group)
        table.groups.remove(group)

    def merge(self, group1: str, group2: str, rename=""):
        gr1 = self._find_unseated_group(group1)
        gr2 = self._find_unseated_group(group2)
        for people in gr1.people:
            gr2.add_people(people)
        self.unseated.remove(gr1)
        if rename != "":
            gr2.set_name(rename)

    def display(self):
        sep = 15 * "-"
        unseated_count = self._count_unseated()
        for table in self.tables:
            table.display()
        print(sep + "\nUnseated ({})\n".format(unseated_count) + sep)
        for group in self.unseated:
            group.display()

    def create_table(self, table_name, capacity=12):
        self.tables.append(Table(name=table_name, capacity=capacity))

    def _assign_assigned(self):
        added_groups = []
        for row in self.raw:
            _, _, gname, tname = row
            if tname != "" and gname not in added_groups:
                self.add(gname, tname)
                added_groups.append(gname)

    def _find_table(self, table_name):
        return filter_by_name(table_name, self.tables)[0]

    def _find_unseated_group(self, group_name):
        return filter_by_name(group_name, self.unseated)[0]

    def _find_seated_group(self, group_name):
        for table in self.tables:
            matching = filter_by_name(group_name, table.groups)
            if len(matching) > 0:
                return matching[0], table

    def _count_unseated(self):
        return sum([g.count for g in self.unseated])

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


def filter_by_name(name, list_of_objects):
    return list(filter(lambda ob: ob.name == name, list_of_objects))
