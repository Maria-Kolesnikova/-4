import csv
import json
INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"
def task() -> None:
    with open("input.csv", "r") as file:
        reader = csv.DictReader(file, delimiter=',', quotechar='"')
        json_data = list(reader)
    with open("output.json", "w") as file:
        json.dump(json_data, file, indent=4)


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")