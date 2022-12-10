def get_input():
    with open('input.txt', encoding='utf-8') as f:
        lines = [line.replace('\n', '') for line in f.readlines()]
        return lines

class Item:
    def __init__(self):
        self.x = 0
        self.y = 0

    def move(self, direction):
        if direction == 'R':
            self.x += 1
        if direction == 'L':
            self.x -= 1
        if direction == 'U':
            self.y += 1
        if direction == 'D':
            self.y -= 1

    def is_touching(self, other):
        if abs(self.x - other.x) <= 1 and abs(self.y - other.y) <= 1:
            return True
        else:
            return False

    def is_in_same_row(self, other):
        return True if self.y == other.y else False

    def is_in_same_column(self, other):
        return True if self.x == other.x else False

class Node:
    def __init__(self, id, data):
        self.id = id
        self.data = data
        self.next = None

def parse_line(line):
    split = line.split(' ')
    return [split[0], int(split[1])]

def build_ll(size):
    i = 2

    head_node = Node(1, Item())
    current_node = head_node 
    
    while i < size + 1:
        new_node = Node(i, Item())
        current_node.next = new_node
        current_node = new_node
        i += 1

    return head_node

def make_moves(first, second):
    if not first.is_touching(second):
        if first.is_in_same_row(second):
            direction = 'R' if first.x - second.x > 0 else 'L'
            second.move(direction)
        elif first.is_in_same_column(second):
            direction = 'U' if first.y - second.y > 0 else 'D'
            second.move(direction)
        else:
            x_direction = 'R' if first.x - second.x > 0 else 'L'
            y_direction = 'U' if first.y - second.y > 0 else 'D'
            second.move(x_direction)
            second.move(y_direction)

def print_map(node, size):
    items = []
    grid = []

    for i in range(0, size):
        grid.append([])

        for j in range(0, size):
            grid[i].append(' ')

    while node:
        position = node.data
        id = node.id
        items.append([id, position])

        node = node.next

    for item in items:
        id = item[0]
        position = item[1]
        grid[position.y][position.x] = id - 1

    grid_str = ""

    for i in range(0, size):
        for j in range(0, size):
            element = grid[size - i - 1][j]
            grid_str += '[' + str(element) +  '] '

        grid_str += '\n'

    print(grid_str)

def pt1():
    lines = get_input()
    size = 10

    start_node = build_ll(size)

    positions = {'00': True}

    for line in lines:
        command = parse_line(line)
        direction, amount = command[0], command[1]

        while amount > 0:
            current_node = start_node
            head = current_node.data

            first = None
            second = None

            head.move(direction)

            while current_node.next:
                first = current_node.data
                second = current_node.next.data

                make_moves(first, second)
                
                if current_node.next.id == size:
                    position_second = str(second.x) + str(second.y)
                    if not positions.get(position_second):
                        positions[position_second] = True

                current_node = current_node.next

            amount -= 1

    return len(positions)

print(pt1())
