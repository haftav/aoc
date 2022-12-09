def main():
    with open("./input.txt", encoding="utf-8") as f:
        current_sum = 0
        max_cals = [0, 0, 0]

        lines = f.read().split("\n")

        for line in lines:
            if line:
                cals = int(line)
                current_sum += cals
            else:
                for i, el in enumerate(max_cals):
                    if current_sum > el:
                        max_cals[i] = current_sum
                        max_cals.sort()
                        break

                current_sum = 0

        print("max: ", sum(max_cals))


main()
