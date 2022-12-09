filename = 'input.txt'

def pt1(input):
    i = 1
    found = False

    while not found:
        if i < 4:
            i += 1
            continue

        chars = input[i-4:i]

        print(chars)

        if len(''.join(set(chars))) == 4:
            found = True
        else:
            i += 1

    return i

def pt2(input):
    i = 1
    found = False

    while not found:
        if i < 14:
            i += 1
            continue

        chars = input[i-14:i]

        print(chars)

        if len(''.join(set(chars))) == 14:
            found = True
        else:
            i += 1

    return i


with open(filename, encoding='utf-8') as f:
    line = f.read().replace('\n', '')
    print(line)
    print(pt2(line))

