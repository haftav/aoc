filename = 'input.txt'

class Stack:
    def __init__(self, name):
        self.name = name
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

class Command:
    def __init__(self, amount, start, end):
        self.amount = amount
        self.start = start - 1
        self.end = end - 1

    def __str__(self):
        return 'amount: ' + str(self.amount) + ', start: ' + str(self.start) + ', end: ' + str(self.end) + '\n'


def get_stack_height(lines):
    i = 1;

    while lines[i][1] != '1':
        i += 1

    return i

def build_stacks(lines):
    stacks = []
    row_index = get_stack_height(lines) - 1

    number_of_stacks = len(lines[row_index].split(' '))

    for i in range(0, number_of_stacks):
        stacks.append(Stack(str(i + 1)))

    while row_index >= 0:
        line = lines[row_index]

        i = 0

        while i < number_of_stacks:
            column_index = i * 4 + 1
            item = line[column_index]

            if item != ' ':
                stacks[i].add(item)
            i += 1

        row_index -= 1

    return stacks


def build_commands(lines):
    commands = []
    for line in lines:
        line = line.replace('move ', '')
        first_split =  line.split(' from ')
        first = first_split[0]
        second_split = first_split[1].split(' to ')
        second = second_split[0]
        third = second_split[1]

        command = Command(int(first), int(second), int(third))
        commands.append(command)

    return commands

def move_stacks(stacks, commands):
    for command in commands:
        amount = command.amount
        start = command.start
        end = command.end


        while amount > 0:
            item = stacks[start].pop()
            stacks[end].add(item)
            amount -= 1

    for stack in stacks:
        print(stack.peek())


def move_stacks_pt_2(stacks, commands):
    for command in commands:
        amount = command.amount
        start = command.start
        end = command.end


        temp_stack = Stack('temp')

        while amount > 0:
            item = stacks[start].pop()

            temp_stack.add(item)

            amount -= 1


        while temp_stack.get_length():
            item = temp_stack.pop()
            stacks[end].add(item)

    for stack in stacks:
        print(stack.peek())


def pt1():
    with open(filename, encoding='utf-8') as f:
        split = f.read().split('\n\n')
        stack_lines, command_lines = split[0].split('\n'), list(filter(lambda line: line, split[1].split('\n')))

        stacks = build_stacks(stack_lines)
        commands = build_commands(command_lines)

        move_stacks(stacks, commands)


def pt2():
    with open(filename, encoding='utf-8') as f:
        split = f.read().split('\n\n')
        stack_lines, command_lines = split[0].split('\n'), list(filter(lambda line: line, split[1].split('\n')))

        stacks = build_stacks(stack_lines)
        commands = build_commands(command_lines)

        move_stacks_pt_2(stacks, commands)

pt2()
