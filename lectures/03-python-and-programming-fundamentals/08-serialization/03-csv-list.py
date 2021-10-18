import csv

def get_sample_data_list():
    return [['T15A', 'Liz', 21],
            ['H12A', 'My Name Has A, Comma In It', 21],
            ['H19A', 'My Name Has A\n newline In It', 21],
            ['H15A', 'William', 21]]

def write_list_as_csv(data, filename):

    # open file for writing (saving)
    f = open(f'files/{filename}.csv', 'w')
    csv_writer = csv.writer(f)

    # write each element in tutorials list, into the file
    for row in data:
        csv_writer.writerow(row)

    # close the file
    f.close()

def read_csv_as_list(filename):
    
    # open file
    f = open(f'files/{filename}.csv', 'r')
    csv_reader = csv.reader(f)

    data = []

    # read in lines from file to data list
    for line in csv_reader:
        data.append(line)

    # close the file
    f.close()

    # return the list
    return data

if __name__=="__main__":
    #my_data = get_sample_data_list()
    #print(my_data)
    #write_list_as_csv(my_data, '03-csv-list')
    my_data = read_csv_as_list('03-csv-list')
    for thing in my_data:
        print(thing)

    my_data.append(['F09A', 'Krishne', 21])
    write_list_as_csv(my_data, '03-csv-list')