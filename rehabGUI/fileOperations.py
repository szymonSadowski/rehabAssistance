def useFile(name, description):
    file = open("save.txt", "a+")
    file.write("Name: " + name + "\r\nDescription " + description + "\r\n")
    file.close()
    readNames()

def readNames():
    file = open("save.txt", "r")
    names = []
    for ln in file:
        if ln.startswith('Name:'):
            lines = ln[6:]
            names.append(lines)
            print(lines)

    file.close()
    return names

