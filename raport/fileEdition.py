import json
import sys
import io
import threading
import time

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

def write_json(data, filename):
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
            write_json(data, 'data.json')
    except IOError as e:
        print(e + "IO ERROR unable to open json")


def give_description(exercise):
    try:
        with open('data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            for name in data['exercises']:
                if name['name'] == exercise:
                    answer = name['description']
            return answer
    except IOError as e:
        print(e + "IO ERROR unable to open json")

# def exercise_json(body_part, x, y):
#     try:
#         with open('exercise.json', encoding='utf-8') as json_file:
#             data = json.load(json_file)
#             temp = data['exercises']
#             # python object to be appended
#             newExercise = {"body_part": body_part, "x": x, "y": y}
#             # print(newExercise)
#             # appending data to emp_details
#             temp.append(newExercise)
#             write_json(data, 'exercise.json')
#             time.sleep(10)
#     except IOError as e:
#         print(e + "IO ERROR unable to open json")


def get_cordinates(exercise,filename):
    centers = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for body_part in data['exercises']:
                if body_part['x'] == exercise:
                    centers.append(body_part['x'])
                if body_part['y'] == exercise:
                    centers.append(body_part['y'])
            return centers
    except IOError as e:
        print(e + "IO ERROR unable to open json")



# robimy słowniki oznaczające 1 klatke, 3 elementy body part = numer kluczowego punktu
# x pozycja x i y pozycja y potem an tej podstawie możemy spróbwać narzucić to na ekran
def save_points(pointsx,pointsy,parts):
    parts = [*parts]
    try:
        with open('exercise.json', encoding='utf-8') as json_file:
            data = json.load(json_file)
            temp = data['exercises']
            # python object to be appended
            newExercise = {"body_part": str(parts), "x": str(pointsx), "y": str(pointsy)}
            # print(newExercise)
            # appending data to emp_details
            temp.append(newExercise)
            write_json(data, 'exercise.json')
            time.sleep(10)
    except IOError as e:
        print(e + "IO ERROR unable to open json")














