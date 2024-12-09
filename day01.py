
r1 = """1122""" # 3 (1 + 2) because the first digit (1)
r2 = """1111""" # 4
r3 = """1234""" # 0
r4 = """91212129""" # 9

def captcha(s):
    matches = []
    s_list = list(s)
    if s_list[-1] == s_list[0]:
        # print(f"{s_list[-1]=}, {s_list[0]=}")
        matches.append(int(s_list[0]))

    # print(f"{s_list=}")
    # print(f"{s_list[1:]=}")
    for d1, d2 in zip(s_list, s_list[1:]):
        # print(f"{d1=}, {d2=}")
        if d1 == d2:
            matches.append(int(d1))
    return sum(matches)

assert captcha(r1) == 3
assert captcha(r2) == 4
assert captcha(r3) == 0
assert captcha(r4) == 9

def main():
    with open("day01.txt", 'r') as f:
        s = f.read().strip()
        print("part 1: ", captcha(s))


if __name__ == "__main__":
    main()
