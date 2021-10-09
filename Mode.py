from collections import Counter
import csv

with open("HeightWeight.csv", newline="") as f:
    reader = csv.reader(f)
    fileData = list(reader)

fileData.pop(0)

newData = []

for i in range(len(fileData)):
    n_num = fileData[i][2]
    newData.append(float(n_num))


data = Counter(newData)
modeDataForRange = {
    "75-85": 0,
    "85-95": 0,
    "95-105": 0,
    "105-115": 0,
    "115-125": 0,
    "125-135": 0,
    "135-145": 0,
    "145-155": 0,
    "155-165": 0,
    "165-175": 0,
}
for weight, occurence in data.items():
    if 75 < weight < 85:
        modeDataForRange["75-85"] += occurence
    elif 85 < weight < 95:
        modeDataForRange["85-95"] += occurence
    elif 95 < weight < 105:
        modeDataForRange["95-105"] += occurence
    elif 105 < weight < 115:
        modeDataForRange["105-115"] += occurence
    elif 115 < weight < 125:
        modeDataForRange["115-125"] += occurence
    elif 125 < weight < 135:
        modeDataForRange["125-135"] += occurence
    elif 135 < weight < 145:
        modeDataForRange["135-145"] += occurence
    elif 145 < weight < 155:
        modeDataForRange["145-155"] += occurence
    elif 155 < weight < 165:
        modeDataForRange["155-165"] += occurence
    elif 165 < weight < 175:
        modeDataForRange["165-175"] += occurence

modeRange, mdoeOccurence = 0, 0
for range, occurence in modeDataForRange.items():
    if occurence > mdoeOccurence:
        modeRange, mdoeOccurence = [
            int(range.split("-")[0]),
            int(range.split("-")[1]),
        ], occurence
mode = float((modeRange[0] + modeRange[1]) / 2)
print(f"The Mode for the given data is: {mode:2f}")

# import statistics as st

# mode = st.mode(newData)
# print(mode)
