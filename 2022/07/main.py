filename = 'input.txt'

class Stack:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def get_length(self):
        return len(self.items)

    def __str__(self):
        out = 'Stack ' + self.name + '\n'
        i = len(self.items) - 1

        while i >= 0:
            out += self.items[i]
            if i != 0:
                out += '\n'
            i -= 1

        return out

def is_file(item):
    return item.type == 'file'

def is_folder(item):
    return item.type == 'folder'

class Folder:
    def __init__(self, name):
        self.type = 'folder'
        self.name = name
        self.children = [] 

    def has_child(self, item):
        for child in self.children:
            if child.type == item.type and child.name == item.name:
                return True
        return False

    def add_child(self, new_child):
        if not self.has_child(new_child):
            self.children.append(new_child)

    def get_child_folder(self, name):
       for child in self.children:
           if is_folder(child) and child.name == name:
               return child

class File:
    def __init__(self, name, size):
        self.type = 'file'
        self.name = name
        self.size = size

class Filesystem:
    def __init__(self):
        root = Folder('/')

        self.dir_stack = Stack()
        self.dir_stack.add(root)

    def get_current_directory(self):
       return self.dir_stack.peek()

    def change_directory(self, arg):
        thing = self.get_current_directory()
        if arg == '/':
            while self.dir_stack.get_length() > 1:
                self.dir_stack.pop()
        elif arg == '..':
            self.dir_stack.pop()
        else:
            current_dir = self.get_current_directory()
            child = current_dir.get_child_folder(arg)

            if not child:
                child = Folder(arg)
                current_dir.add_child(child)

            self.dir_stack.add(child)

def get_command(line):
    split = line.split(' ')
    name = split[1]

    if name == 'cd':
        return [split[1], split[2]]

    return [split[1]]

def is_command(line):
    return True if line[0] == '$' else False

def is_cd(command):
    return True if command[0] == 'cd' else False

def is_ls(command):
    return True if command[0] == 'ls' else False


def get_result(line):
    split = line.split(' ')

    return split


def is_dir_result(result):
    if result[0] == 'dir':
        return True
    else:
        return False

def traverse(item, prefix='/', seen={}, folders = [], depth = 0):
    if is_file(item):
        return
    else:
        full_prefix = prefix + '-' + item.name

        if not seen.get(full_prefix):
            folders.append(item)
            seen[full_prefix] = True

            for child in item.children:
                traverse(child, prefix + item.name, seen, folders,  depth + 4)

    return folders


def get_folder_size(item, sum = 0):
    if is_file(item):
        return int(item.size)
    else:
        for child in item.children:
            sum = sum + get_folder_size(child)

        return sum

def get_fs():
    with open(filename, encoding='utf-8') as f:
        fs = Filesystem()

        lines = [line.replace('\n', '') for line in f.readlines()]

        last_command = None

        for line in lines:
            if is_command(line):
                command = get_command(line)

                last_command = command[0]

                if is_cd(command):
                    fs.change_directory(command[1])
            else:
                if last_command == 'ls':
                    result = get_result(line)
                    new_child = Folder(result[1]) if is_dir_result(result) else File(result[1], result[0])

                    fs.get_current_directory().add_child(new_child)

        fs.change_directory('/')

        return fs

def pt1():
        fs = get_fs()
        sum = 0
        
        folders = traverse(fs.get_current_directory())

        for folder in folders:
            size = get_folder_size(folder)

            if size <= 100000:
                sum += size

        return sum

def pt2():
        fs = get_fs()
        fs_size = get_folder_size(fs.get_current_directory())

        unused_space = 70000000 - fs_size
        min_size = 30000000 - unused_space
        print('min size', min_size)

        smallest = None
        
        folders = traverse(fs.get_current_directory())


        for folder in folders:
            size = get_folder_size(folder)
            print('size', size)

            if size >= min_size:
                print('is appropriate size', smallest, size)
                print(not smallest or size <= smallest)
                if not smallest or size <= smallest:
                    smallest = size

        return smallest
print(pt2())
