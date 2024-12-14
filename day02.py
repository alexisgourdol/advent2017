from itertools import combinations


def main():
    with open("day02.txt") as f:
        lines = f.readlines()
    lines = [l.split() for l in lines]
    lines = [[int(el) for el in l] for l in lines]

    print("part 1: ", sum([max(l) - min(l) for l in lines]))

    res = []
    for l in lines:
        for a, b in combinations(l, 2):
            if a != b and a % b == 0:
                res.append(a // b)
                break

            if a != b and b % a == 0:
                res.append(b // a)
                break
    print("part 2: ", sum(res))


if __name__ == "__main__":
    main()
