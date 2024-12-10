def captcha(s: str) -> int:
    matches = []
    s_list = list(s)
    if s_list[-1] == s_list[0]:
        matches.append(int(s_list[0]))

    for d1, d2 in zip(s_list, s_list[1:]):
        if d1 == d2:
            matches.append(int(d1))
    return sum(matches)

def captcha_2(s: str) -> int:
    assert len(s) % 2 == 0
    steps = len(s) // 2
    matches = []
    s_list = list(s)

    # for every el in the list, spot the value N steps ahead
    for i, d1 in enumerate(s_list):
        d2 = s_list[(i + steps) % len(s_list)]
        if d1 == d2:
            matches.append(int(d1))
    return sum(matches)

r1 = """1122""" # 3 (1 + 2) because the first digit (1)
r2 = """1111""" # 4
r3 = """1234""" # 0
r4 = """91212129""" # 9

assert captcha(r1) == 3
assert captcha(r2) == 4
assert captcha(r3) == 0
assert captcha(r4) == 9


r5 = """1212""" # 6
r6 = """1221""" # 0
r7 = """123425""" # 4
r8 = """123123""" # 12
r9 = """12131415""" # 4

assert captcha_2(r5) == 6
assert captcha_2(r6) == 0
assert captcha_2(r7) == 4
assert captcha_2(r8) == 12
assert captcha_2(r9) == 4

def main():
    with open("day01.txt", 'r') as f:
        s = f.read().strip()
    print("part 1: ", captcha(s))
    print("part 2: ", captcha_2(s))

if __name__ == "__main__":
    main()
