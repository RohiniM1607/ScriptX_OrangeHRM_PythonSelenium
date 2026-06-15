import csv

def get_data_csv(filename):
    data = []
    path = "Configurations/"+filename
    with open(path, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            data.append(row)

    return data