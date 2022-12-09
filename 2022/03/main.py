import string
filepath = 'input.txt'

def find_error(comp_1, comp_2):
    for char in comp_2:
        if char in comp_1:
            return char

def get_score(char):
    if char in string.ascii_lowercase:
        return ord(char) % 97 + 1
    else:
        return ord(char) % 65 + 27
    

def pt1():
    score = 0

    with open(filepath, encoding='utf-8') as f:
        for line in f.read().split("\n"):
            if line:
                midpoint = int(len(line) / 2)
                comp_1, comp_2 = line[0:midpoint], line[midpoint:]
                char = find_error(comp_1, comp_2)
                score += get_score(char)

    print(score)
    return score


def get_badge(lines):
    set_one = ''.join(set(lines[0]))
    set_two = ''.join(set(lines[1]))

    for char in lines[2]:
        if char in set_one and char in set_two:
            return char


def pt2():
    score = 0
    index = 0

    with open(filepath, encoding='utf-8') as f:
        lines = f.read().split("\n")
        while index < len(lines) - 3:
            group_lines = lines[index:index + 3]

            badge = get_badge(group_lines)
            score += get_score(badge)
            index += 3
    return score

pt2()
