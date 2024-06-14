#data_formatter.py
import csv,operator,sys
dataset = []
def data_formatter(datafile):
    with open(datafile) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            dataset.append(row)
            line_count += 1
    dataset[1:] = sorted(dataset[1:], key=operator.itemgetter(1))    # 0 specifies according to first column we want to sort
    
    dataset[0].append('<NEXT_DAY_HIGHT>')
    dataset[0].append('<NEXT_DAY_CLOSE>')
    for i, row in enumerate(dataset[1:-1], 1):
        row.append(dataset[i+1][3])
        row.append(dataset[i+1][5])

    with open('File_FORMATTED.csv', mode='w', newline='') as file_shit:
        shit_writer = csv.writer(file_shit, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in dataset:
            shit_writer.writerow(row)

datafile1 = "Goltash.csv"
data_formatter(datafile1)