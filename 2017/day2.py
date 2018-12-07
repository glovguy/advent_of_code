import csv
import re


check_sum = 0

with open('day2_data.csv', 'r') as csvFile:
    for eachRow in csvFile:
        row = [int(x) for x in eachRow.split()]
        check_sum += max(row) - min(row)

print("Part one check sum: ")
print(check_sum)


div_sum = 0

def row_sum(row):
    item = row.pop()
    for i in row:
        if item % i == 0:
            return item / i
    return row_sum(row)


with open('day2_data.csv', 'r') as csvFile:
    for eachRow in csvFile:
        row = [int(x) for x in eachRow.split()]
        row.sort()
        div_sum += row_sum(row)

print("Part two check sum: ")
print(div_sum)

div_sum2 = 0
with open('day2_data.csv', 'r') as csvFile:
    div_sum2 += [int(x) for eachRow in csvFile for x in eachRow.split()]
print("Part two check sum: ")
print(div_sum2)