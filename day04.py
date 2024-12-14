from itertools import combinations

with open("day04.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

valid_passphrases = 0
for line in lines:
    if len(line.split()) == len(set(line.split())):
        valid_passphrases += 1
print("part 1: ", valid_passphrases)

valid_passphrases_2 = 0
for line in lines:
    words = line.split()
    # compare each pair of words to detect any anagrams
    for w1, w2 in combinations(words, 2):
        print(f"w1: {w1}, w2: {w2}")
        if sorted(w1) == sorted(w2):
            break
    else:
        valid_passphrases_2 += 1

print("part 2: ", valid_passphrases_2)
