import csv


class TableList:
    def __init__(self):
        self.tables = []

    def export(self):
        for table in self.tables:
            table.display()
