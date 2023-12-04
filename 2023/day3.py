import re

with open("2023/input_day3.txt", "r") as f:
    total = 0
    lines = f.readlines()
    l = len(lines[0])
    h = len(lines)
    for i in range(0, h):
        line = lines[i]
        matches = re.finditer(r"(\d+)", line)
        for m in matches:
            start = m.start()
            end = m.end()
            if (start > 0 and line[start-1] != ".") or \
                (end+1 <= l-1 and line[end] != ".") or \
                (i > 0 and re.match(r".*[^\.\d].*", lines[i-1][max(start-1,0):min(end+1,l-1)]) is not None) or \
                (i+1 < h and re.match(r".*[^\.\d].*", lines[i+1][max(start-1,0):min(end+1,l-1)]) is not None):
                total += int(m.group(1))
    print(total)
