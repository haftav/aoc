filename = 'test.txt'

class Folder:
    def __init__(self, id):
        self.id = id
        self.children = {}

        print('init')
    def add_child(self, id):
        if not self.children[id]

class File:
    def __init__(self, size):
        self.size = size
        print('init')

class Filesystem:
    def __init__(self):
        self.current_folder = Folder('/')


def is_command(line):
    return True if line[0] == '$' else False

def get_command(line):
    split = line.split(' ')
    name = split[1]

    if name == 'cd':
        return [split[1], split[2]]

    return [split[1]]

def is_command(line):
    return True if line[0] == '$' else False

def is_file():
    print('is_file')

def is_folder():
    print('is_folder')

def pt1():
    with open(filename, encoding='utf-8') as f:
        lines = [line.replace('\n', '') for line in f.readlines()]
        for line in lines:
            if is_command(line):
                command = get_command(line)
                print(command)



pt1()
