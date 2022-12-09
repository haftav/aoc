filename = 'input.txt'

def get_range(sections):
    split = sections.split('-')
    min, max = int(split[0]), int(split[1])
    return (min, max)

def is_fully_contained(range1, range2):
    range1_min, range1_max = range1[0], range1[1]
    range2_min, range2_max = range2[0], range2[1]

    if range1_min >= range2_min and range1_max <= range2_max:
        return True

    if range2_min >= range1_min and range2_max <= range1_max:
        return True

    return False


def has_overlap(range1, range2):
    range1_min, range1_max = range1[0], range1[1]
    range2_min, range2_max = range2[0], range2[1]

    if range1_min >= range2_min and range1_min <= range2_max:
        return True

    if range2_min >= range1_min and range2_min <= range1_max:
        return True

    return False

def pt1():
    count = 0
    with open(filename, encoding='utf-8') as f:
        for line in f.read().split('\n'):
            if line:
                split = line.split(',')
                first_elf_sections, second_elf_sections = split[0], split[1]
                first_elf_range, second_elf_range = get_range(first_elf_sections),get_range(second_elf_sections)
                if is_fully_contained(first_elf_range, second_elf_range):
                    count += 1

    print(count)

def pt2():
    count = 0
    with open(filename, encoding='utf-8') as f:
        for line in f.read().split('\n'):
            if line:
                split = line.split(',')
                first_elf_sections, second_elf_sections = split[0], split[1]
                first_elf_range, second_elf_range = get_range(first_elf_sections),get_range(second_elf_sections)
                if has_overlap(first_elf_range, second_elf_range):
                    count += 1

    print(count)

pt2()
