
def run(instructions: list) -> int:
    pos = 0
    steps = 0
    next_position = 0

    while 0 <= pos < len(instructions):
        if instructions[pos] == 0:
            # update instructions and stay at current position
            instructions[pos] += 1
            steps += 1
        else:
        # update instructions and move to next position
            next_position = instructions[pos]
            instructions[pos] += 1
            pos += next_position
            steps += 1
    return steps

def run_2(instructions: list) -> int:
    pos = 0
    steps = 0
    next_position = 0
    # print(f"{steps=} | {instructions=}")
    while 0 <= pos < len(instructions):
        if instructions[pos] == 0:
            # update instructions and stay at current position
            instructions[pos] += 1
            steps += 1
        else:
            # update instructions and move to next position
            if instructions[pos] < 3:
                next_position = instructions[pos]
                instructions[pos] += 1
                pos += next_position
                steps += 1
            else:
                next_position = instructions[pos]
                instructions[pos] -= 1
                pos += next_position
                steps += 1
        #print(f"{steps=} | {pos=} |{instructions[:10]=}")
        #print(f"                |                 ={ ['^' if i == pos else 0 for i, el in enumerate(instructions[:10])] }")
    return steps

RAW = """0
3
0
1
-3
"""
"""
(0) 3  0  1  -3  - before we have taken any steps.
(1) 3  0  1  -3  - jump with offset 0 (that is, don't jump at all). Fortunately, the instruction is then incremented to 1.
 2 (3) 0  1  -3  - step forward because of the instruction we just modified. The first instruction is incremented again, now to 2.
 2  4  0  1 (-3) - jump all the way to the end; leave a 4 behind.
 2 (4) 0  1  -2  - go back to where we just were; increment -3 to -2.
 2  5  0  1  -2  - jump 4 steps forward, escaping the maze.
"""
test_instructions = [int(el) for el in RAW.strip().split('\n')]
test_instructions_2 = test_instructions.copy()
print("test part 1: ", run(test_instructions))  # 5
# print("test part 2: ", run_2(test_instructions_2))  # 8


if __name__ == "__main__":
    with open('day05.txt') as f:
        instructions = [int(el) for el in f.readlines()]
    instructions_2 = instructions.copy()
    print("part 1: ", run(instructions)) # 356687 wrong, too low ; 358309 ok
    print("part 2: ", run_2(instructions_2)) # 2529 too low
