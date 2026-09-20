import itertools
import json
import time

ROW = 8

# step 9: find fitting strings for row (product ends in 1)
rows = {
    0: [0, 0, 1, 0, 0, 1, 0, 1, 0, 0],
    8: [0, 1, 1, 1, 1, 0, 1, 0, 1, 1],
    9: [0, 1, 0, 0, 1, 0, 1, 0, 0, 0],  # right
    10: [1, 0, 1, 0, 0, 1, 1, 0, 0, 1],  # right
    11: [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],  # right
}

row = rows[ROW]


options = [
    "x1379",  # since (8, 2) has to be in"1379"
    "1379",
    "x0123456789",
    "x0123456789",
    "x0123456789",
    "x0123456789",
    "x0123456789",
    "x0123456789",
    "x0123456789",
    "0123456789",
    "x0123456789",
]
tot = 1
for option in options:
    tot *= len(option)

# Generate all combinations
print("Starting")
print("generating combinations")
t0 = time.time()
all_combinations = itertools.product(*options)

print("Total combinations", tot)
print("Time taken", time.time() - t0)


def does_string_fit_row(s: str, row: list):
    if "xx" in s:
        return False

    for j in range(10):
        if "x" != s[j] and "x" != s[j + 1]:
            if row[j] == 0 and s[j] != s[j + 1]:
                return False
            if row[j] == 1 and s[j] == s[j + 1]:
                return False

    return True


# Print each combination as a string
i = 0
WINS = []
t0 = time.time()
for combination in all_combinations:
    s = "".join(combination)
    i += 1
    if i % (int(tot / 100 / 200)) == 0:
        print(
            "Percent",
            int(200 * i * 100 / tot) / 200,  # this prints two decimals
            "Time Remaining",
            int((time.time() - t0) * (tot - i) / (i * 60)),
        )

    if does_string_fit_row(s, row):
        nums = s.split("x")
        for num in nums:
            if num == "":
                continue
            if len(num) == 1 or num[0] == "0":
                break

            if num != num[::-1]:
                break
            if int(num) % 23 != 0:
                break
        else:
            WINS.append(s)

            with open(f"row_{ROW}.json", "w") as f:
                json.dump(WINS, f, indent=2)


print("Done")
