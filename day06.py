from time import sleep
# sixteen memory banks

"""
For example, imagine a scenario with only four memory banks:

- The banks start with 0, 2, 7, and 0 blocks. The third bank has the most blocks,
so it is chosen for redistribution.
- Starting with the next bank (the fourth bank) and then continuing to the first bank,
the second bank, and so on, the 7 blocks are spread out over the memory banks. The fourth,
 first, and second banks get two blocks each, and the third bank gets one back. The final
   result looks like this: 2 4 1 2.
- Next, the second bank is chosen because it contains the most blocks (four). Because
there are four memory banks, each gets one block. The result is: 3 1 2 3.
- Now, there is a tie between the first and fourth memory banks, both of which have three
 blocks. The first bank wins the tie, and its three blocks are distributed evenly over the
   other three banks, leaving it with none: 0 2 3 4.
- The fourth bank is chosen, and its four blocks are distributed such that each of the
four banks receives one: 1 3 4 1.
- The third bank is chosen, and the same thing happens: 2 4 1 2.

"""
#memory_banks = {idx + 1: int(el) for idx, el in enumerate(RAW.split())}


def reallocation_routine(memory_banks: list) -> int:
    seen = set()
    block_redistribution_cycle = 0
    memory_banks_cycle = {}

    while True:
        max_index = memory_banks.index(max(memory_banks))
        max_value = memory_banks[max_index]
        memory_banks[max_index] = 0
        for i in range(0, max_value):
            # cycle over the memory banks list
            memory_banks[(max_index + i + 1) % len(memory_banks)] += 1
        block_redistribution_cycle += 1
        if not memory_banks_cycle.get(tuple(memory_banks)):
            memory_banks_cycle[tuple(memory_banks)] = []
        memory_banks_cycle[tuple(memory_banks)].append(block_redistribution_cycle)
        if tuple(memory_banks) in seen:
            already_seen = tuple(memory_banks)
            num_cycles_to_seen_again = (memory_banks_cycle[already_seen][1] - memory_banks_cycle[already_seen][0])
            break
        else:
            seen.add(tuple(memory_banks))
    return block_redistribution_cycle, num_cycles_to_seen_again

RAW = """0  2   7   0"""
test_memory_banks = [int(el) for el in RAW.split()]
test_memory_banks = test_memory_banks[:]
assert reallocation_routine(test_memory_banks) == (5, 4)


with open("day06.txt") as f:
    raw = f.read().strip()
original_memory_banks = [int(el) for el in raw.split()]
memory_banks = original_memory_banks[:]


print("part 1: ", reallocation_routine(memory_banks)[0])
print("part 2: ", reallocation_routine(memory_banks)[1])
