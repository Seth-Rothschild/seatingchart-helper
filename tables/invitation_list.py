import csv


class InvitationList:
    def __init__(self, csv_path=""):
        self.raw = []
        if csv_path != "":
            self.read_csv(csv_path)

    def read_csv(self, csv_path):
        with open(csv_path) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=",")
            for row in readCSV:
                name, count = row
                self.raw.append((name, int(count)))
