def get_input():
    with open('input.txt', encoding='utf-8') as f:
        lines = [line.replace('\n', '') for line in f.readlines()]
        return lines

def is_visible_top(height, start_row, column, lines):
    row = start_row

    while row >= 0:
        top_tree_height = lines[row][column]
        if height <= top_tree_height:
            return False
        row -= 1

    return True

def get_top_score(height, start_row, column, lines):
    row = start_row
    score = 0

    while row >= 0:
        score += 1
        top_tree_height = lines[row][column]

        if height <= top_tree_height:
            break
        row -= 1

    print('top score', score)
    return score

def is_visible_bottom(height, start_row, column, lines):
    row = start_row

    while row < len(lines):
        bottom_tree_height = lines[row][column]

        if height <= bottom_tree_height:
            return False
        row += 1

    return True

def get_bottom_score(height, start_row, column, lines):
    row = start_row
    score = 0

    while row < len(lines):
        score += 1
        bottom_tree_height = lines[row][column]

        print('compare heights', height, bottom_tree_height)

        if height <= bottom_tree_height:
            break
        row += 1

    print('bottom score', score)
    return score

def is_visible_right(height, row, start_column, lines):
    column = start_column

    while column < len(lines):
        right_tree_height = lines[row][column]
        if height <= right_tree_height:
            return False
        column += 1

    return True

def get_right_score(height, row, start_column, lines):
    column = start_column
    score = 0

    while column < len(lines):
        score += 1
        right_tree_height = lines[row][column]
        if height <= right_tree_height:
            break
        column += 1

    print('right score', score)
    return score

def is_visible_left(height, row, start_column, lines):
    column = start_column

    while column >= 0:
        left_tree_height = lines[row][column]
        if height <= left_tree_height:
            return False
        column -= 1

    return True

def get_left_score(height, row, start_column, lines):
    column = start_column
    score = 0

    while column >= 0:
        score += 1
        left_tree_height = lines[row][column]
        if height <= left_tree_height:
            break
        column -= 1

    print('left score', score)
    return score


def is_visible(height, row, column, lines):
    return is_visible_top(height, row - 1, column, lines) \
        or is_visible_right(height, row, column + 1, lines) \
        or is_visible_bottom(height, row + 1, column, lines) \
        or is_visible_left(height, row, column - 1, lines)

def get_surrounding_trees(row, column, lines):
    top = lines[row - 1][column]
    right = lines[row][column + 1]
    bottom = lines[row + 1][column]
    left = lines[row][column - 1]

    return [top, right, bottom, left]


def pt1():
    lines = get_input()

    visible_trees = 0

    i = 1

    while i < len(lines[0]) - 1:
        j = 1

        while j < len(lines) - 1:
            height = lines[i][j]

            if is_visible(height, i, j, lines):
                visible_trees += 1

            j += 1

        i += 1

    return visible_trees + (len(lines) - 1) * 4


def get_scenic_score(height, row, column, lines):
    return get_top_score(height, row - 1, column, lines) \
         * get_right_score(height, row, column + 1, lines) \
         * get_bottom_score(height, row + 1, column, lines) \
         * get_left_score(height, row, column - 1, lines)

def pt2():
    lines = get_input()

    highest_score = 0

    i = 1

    while i < len(lines[0]) - 1:
        j = 1

        while j < len(lines) - 1:
            height = lines[i][j]

            score = get_scenic_score(height, i, j, lines)

            if score > highest_score:
                highest_score = score

            j += 1

        i += 1

    return highest_score

print(pt2())

