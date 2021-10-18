import os

def get_sample_data():
    return ["hello", "how are you?", "that's good",
            "nice to meet you", "goodbye\nI'll see you again"]

def write_file(data, filename):
    # open file
    f = open(f'files/{filename}.txt', 'w')

    # write contents
    for text in data:
        f.write(text + os.linesep)

    # close file
    f.close()

def read_file(filename):
    # open
    f = open(f'files/{filename}.txt', 'r')

    # read the contents
    data = []
    for line in f.readlines():
        data.append(line.strip())

    # close the file
    f.close()

    return data

if __name__ == "__main__":
    #my_data = get_sample_data()
    #write_file(my_data, '02-plain-text')
    my_data = read_file('02-plain-text')
    print(my_data)
