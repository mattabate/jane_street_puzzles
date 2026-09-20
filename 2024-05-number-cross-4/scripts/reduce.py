import json
import fire


def main(row: str):
    file = f"row_{row}.json"

    with open(file) as f:
        rows = json.load(f)

    chars = ["" for _ in range(11)]

    for i in range(11):
        for row in rows:
            if row[i] not in chars[i]:
                chars[i] += row[i]

    print(chars)


if __name__ == "__main__":
    fire.Fire(main)
