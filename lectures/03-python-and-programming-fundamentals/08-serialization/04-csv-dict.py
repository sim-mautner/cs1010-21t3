import csv

def get_sample_data_dict():
    return [{'tutorial':'T15A', 'tutor':'Liz', 'enrollments':21},
            {'tutorial':'H12A', 'tutor':'My Name Has A, Comma In It', 'enrollments':21},
            {'tutorial':'H15A', 'tutor':'William', 'enrollments':21}]

def write_dict_as_csv(data, filename, fieldnames):
    f = open(f'files/{filename}.csv', 'w', newline='')
    csv_writer = csv.DictWriter(
        f, fieldnames=fieldnames
    )
    csv_writer.writeheader()
    for row in data:
        csv_writer.writerow(row)

    f.close()

def read_csv_as_dict(filename):
    # create empty list to read the file into
    data = []

    # open the file
    f = open(f'files/{filename}.csv', 'r')

    # create a dictionary reader
    csv_reader = csv.DictReader(f)

    # read in the file
    for row in csv_reader:
        data.append(row)

    # close the file
    f.close()

    # return the information read in
    return data

if __name__=="__main__":
    #my_data = get_sample_data_dict()
    #write_dict_as_csv(my_data, '04-csv-dict', ['tutor','tutorial','enrollments'])
    my_data = read_csv_as_dict('04-csv-dict')
    print(my_data)
