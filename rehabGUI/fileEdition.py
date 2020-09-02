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

def exercise_json(body_part, x, y):
    try:
        with open('exercise.json', encoding='utf-8') as json_file:
            data = json.load(json_file)
            temp = data['exercises']
            # python object to be appended
            newExercise = {"body_part": body_part, "x": x, "y": y}
            # print(newExercise)
            # appending data to tmp_details
            temp.append(newExercise)
            write_json(data, 'exercise.json')
    except IOError as e:
        print(e + "IO ERROR unable to open json")


def get_cordinates(filename):
    centers = []
    temp = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for body_part in data['exercises']:
                body_part['x'] = temp.append(body_part['x'])
                body_part['y'] = temp.append(body_part['y'])
                centers.append(temp)
                temp = []
            return centers

    except IOError as e:
        print(e + "IO ERROR unable to open json")



def get_cordinatesX(filename):
    centersX = []
    tempX = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for body_part in data['exercises']:
                body_part['x'] = tempX.append(body_part['x'])
                for x in tempX:
                    centersX.append(x)
                tempX = []

            return centersX
    except IOError as e:
        print(e + "IO ERROR unable to open json")


def get_cordinatesY(filename):
    centersY = []
    tempY = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for body_part in data['exercises']:
                body_part['y'] = tempY.append(body_part['y'])
                for y in tempY:
                    centersY.append(y)
                tempY = []
            return centersY
    except IOError as e:
        print(e + "IO ERROR unable to open json")

def pointsPlacment(filename):
    points = []
    tempPoint = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for body_part in data['exercises']:
                body_part['body_part'] = tempPoint.append(body_part['body_part'])
                for body_part in tempPoint:
                    points.append(body_part)
                tempPoint = []
            return points
    except IOError as e:
        print(e + "IO ERROR unable to open json")


# this function takes filename and nuber of iterations and gives information about
# how many key points are in each element
def get_bodyParts(filename, iteration):
    # numberOfIterations is used to count number of elements in json then checking with
    # iteration which is send from main program
    # numberOfKeyPoints is number of body part points in each dictionatry selected by main program
    numberOfIterations = 0
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for body_part in data['exercises']:
                numberOfIterations = numberOfIterations + 1
                if numberOfIterations == iteration:
                    numberOfKeyPoints = (body_part['body_part'])
                    numberOfKeyPoints = Convert(numberOfKeyPoints)
                    numberOfKeyPoints = len(numberOfKeyPoints)
            return numberOfKeyPoints
    except IOError as e:
        print(e + "IO ERROR unable to open json")

# gives you number needed to get through whole file
def get_numberOfIterations(filename):
    counter = 0
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for body_part in data['exercises']:
                counter = counter + 1
            return counter
    except IOError as e:
        print(e + "IO ERROR unable to open json")

# converts strings to list (very important because imported json info is string)
def Convert(string):
    li = list(string.split(" "))
    return li










