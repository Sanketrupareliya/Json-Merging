import json
from pathlib import Path


with open(r'json merging2\one.json') as json_file:
    data1 = json.load(json_file)
with open(r'json merging2\two.json') as json_file:
    data2 = json.load(json_file)


data3 = data1.copy()
cord = [0]*len(data1)

for i in range(len(data1)):
    ord = []
    for j in data2:
        if(data1[i]["process_id"] == j["process_id"]):
            data3[i].update({"status": j["status"]})
            break
        if(data1[i]["process_id"] == j["parent_process_id"]):
            ord.append(j["status"])
    cord[i] = ord.copy()
    print(cord[i])
    if(len(data3[i]) < 3):
        if("PASSED" in cord[i]):
            data3[i].update({"status": "PASSED"})
        elif("NEEDS_MANUAL_REVIEW" in cord[i]):
            data3[i].update({"status": "NEEDS_MANUAL_REVIEW"})
        elif("IN_PROGRESS" in cord[i]):
            data3[i].update({"status": "IN_PROGRESS"})
        elif("FAILED" in cord[i]):
            data3[i].update({"status": "FAILED"})
        elif(len(cord[i]) == 0):
            data3[i].update({"status": None})

with open(r'json merging2\merged.json', "w") as merge:
    json.dump(data3, merge)
