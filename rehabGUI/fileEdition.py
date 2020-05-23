import json
import sys
import io

def read_json():
    try:
        with open('data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except IOError as e:
        print(e + "IO ERROR unable to open json")

def give_names():
    names = []
    try:
        with open('data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            for name in data['exercises']:
                names.append(name['name'])
            return names
    except IOError as e:
        print(e + "IO ERROR unable to open json")

def write_json(data, filename='data.json'):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except IOError as e:
        print(e + "IO ERROR unable to open json")

def append_json(name, description):
    try:
        with open('data.json', encoding='utf-8') as json_file:
            data = json.load(json_file)
            temp = data['exercises']
            # python object to be appended
            newExercise = {"name": name, "description": description}
            # print(newExercise)
            # appending data to emp_details
            temp.append(newExercise)
            write_json(data)
    except IOError as e:
        print(e + "IO ERROR unable to open json")
