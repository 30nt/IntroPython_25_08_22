import csv


def csv_dict_reader(filename: str):
    data = []
    with open(filename, 'r') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=";")
        for row in reader:
            data.append(row)
    return data


def csv_dict_writer(filename: str, data: list):
    fieldnames = list(data[0].keys())
    with open(filename, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


filename = "data.csv"
data = csv_dict_reader(filename)
print(data)

for row in data:
    row['Sum'] = str(int(row['One']) + int(row["Two"]))


# data.append([100, 200, 300])
#
filename = "output.csv"
data = csv_dict_writer(filename, data)

# def csv_reader(filename: str):
#     data = []
#     with open(filename, 'r') as csv_file:
#         reader = csv.reader(csv_file, delimiter=";")
#         for row in reader:
#             data.append(row)
#     return data
#
#
# def csv_writer(filename: str, data: list):
#     with open(filename, 'w') as csv_file:
#         writer = csv.writer(csv_file)
#         writer.writerows(data)
#
#
# filename = "data.csv"
# data = csv_reader(filename)
# print(data)
#
# data.append([100, 200, 300])
#
# filename = "output.csv"
# data = csv_writer(filename, data)
