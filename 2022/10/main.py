def get_input():
    with open('input.txt', encoding='utf-8') as f:
        lines = [line.replace('\n', '') for line in f.readlines()]
        return lines

def get_command(line):
    return line.split(' ')

def is_sprite_over_pixel(x, sprite_x):
    if x >= sprite_x - 1 and x <= sprite_x + 1:
        return True
    else:
        return False

def get_pixel(x, sprite_x):
    if is_sprite_over_pixel(x, sprite_x):
        return '#'
    else:
        return '.'

def print_screen(screen):
    output = ''
    for line in screen:
        output += ''.join(line)
        output += '\n'

    print(output)

def pt2():
    sprite_center = 1
    cycles = 0
    sum = 0

    screen = []

    lines = get_input()

    for line in lines:
        command = get_command(line)
        name = command[0]
        num_cycles_to_add = 1


        if name == 'addx':
            num_cycles_to_add += 1

        while num_cycles_to_add > 0:
            row = cycles // 40
            column = cycles % 40

            if column == 0:
                thing = ' ' * 40
                screen.append(thing.split(' '))

            screen[row][column] = get_pixel(column, sprite_center)

            cycles += 1

            num_cycles_to_add -= 1

        if name == 'addx':
            sprite_center += int(command[1])

    print_screen(screen)
    return sum


print(pt2())
