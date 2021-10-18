import json

def get_sample_data():
    return [ 
        {'tutorial': 'T15A', 'tutor': 'Sim', 'enrollments': 20},
        {'tutorial': 'T17A', 'tutor': 'Kai', 'enrollments': 23},
        {'tutorial': 'T17A', 'tutor': 'Ka\ni', 'enrollments': 23},
        ]

# For complex data structures
def get_sample_data_complex():
    return {
        "fridge": ["chiller", "door", "shelves"],
        "dishwasher": ["motor", "rack", "tube"],
        "vacuum": ["hose", "motor", "bag"]}

def write_json_file(data, filename):
    # open
    f = open(f'files/{filename}.json', 'w')
    # write
    f.write(json.dumps(data))
    # close
    f.close()

def read_json_file(filename):
  # open
  f = open(f'files/{filename}.json', 'r')
  # read
  data = json.loads(f.read())
  # close
  f.close()
  return data

if __name__=="__main__":
    #my_data = get_sample_data()
    #write_json_file(my_data, '05-json')
    #my_data = read_json_file('05-json')
    #for item in my_data:
    #    print(item)

    #my_data = get_sample_data_complex()
    #write_json_file(my_data, '05-json-complex')
    my_data = read_json_file('05-json-complex')
    for item,value in my_data.items():
        print(item)
        print(value)

    my_data["mop"] = ['handle', 'head']

    write_json_file(my_data, '05-json-complex')