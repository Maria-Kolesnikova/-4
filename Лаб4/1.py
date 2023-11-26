
import json
with open('input.json', 'r') as file:
    data = json.load(file)
def task(data):
    total_sum = sum(i["score"] * i["weight"] for i in data)
    rounded_sum = round(total_sum, 3)
    return rounded_sum
print(task(data))