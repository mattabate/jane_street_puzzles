import json
import tqdm


ROW1 = 10
ROW2 = ROW1 + 1

rows_1_file = f"row_{ROW1}.json"
rows_2_file = f"row_{ROW2}.json"
save_file = f"merge_{ROW1}_{ROW2}.json"
vals_1_file = f"vals_{ROW1}.json"
vals_2_file = f"vals_{ROW2}.json"

with open(rows_1_file) as f:
    strings_set1 = json.load(f)
with open(rows_2_file) as f:
    strings_set2 = json.load(f)


col_rol = {
    4: [1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1],
    5: [1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0],
    6: [0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0],
    7: [1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
    8: [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    9: [1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0],  # 9, 10
    10: [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1],  # 10, 11
}
col_rol = col_rol[ROW1]

out = {}
for s1 in tqdm.tqdm(strings_set1):
    out[s1] = []
    for s2 in strings_set2:
        for i in range(11):
            if s1[i] == "x" and s2[i] == "x":
                break  # bad
            if s1[i] == "x" or s2[i] == "x" or col_rol[i] == 0:
                continue
            if s1[i] != s2[i]:
                break
        else:
            out[s1].append(s2)

    if not out[s1]:
        del out[s1]

with open(save_file, "w") as f:
    json.dump(out, f)


def collect_ith_characters(strings):
    # Assume all strings are of the same length, here length 11
    length_of_strings = 11
    # Create a list of sets for each position
    character_sets = [set() for _ in range(length_of_strings)]

    # Iterate over each string in the list
    for s in strings:
        # For each string, update the set corresponding to each position
        for i in range(length_of_strings):
            character_sets[i].add(s[i])

    out = []
    for c in character_sets:
        out.append("".join(list(c)))
    return out


print(f"Row {ROW1}")
new_row_1 = [x for x in out.keys()]
print(json.dumps(collect_ith_characters(new_row_1), indent=1))

with open(vals_1_file, "w") as f:
    json.dump(collect_ith_characters(new_row_1), f)

print(f"row {ROW2}")
new_row_2 = []
for k in new_row_1:
    new_row_2.extend(out[k])
new_row_2 = list(set(new_row_2))
print(json.dumps(collect_ith_characters(new_row_2), indent=1))

with open(vals_2_file, "w") as f:
    json.dump(collect_ith_characters(new_row_2), f)

with open(rows_1_file, "w") as f:
    json.dump(new_row_1, f)

with open(rows_2_file, "w") as f:
    json.dump(new_row_2, f)
