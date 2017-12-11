from day9_data import stream
# stream='<{o"i!a,<{i<a>'

bracket_stack = []
garbage_stack = []
group_count = 0
group_score = 0
garbage_char_count = 0
skip = False

for symbol in stream:
    if skip == True:
        skip = False
        continue

    if symbol == '!':
        skip = True
        continue

    if symbol == '<' and len(garbage_stack) == 0:
        garbage_stack.append(1)
        continue

    if symbol == '>' and len(garbage_stack) > 0:
        garbage_stack.pop()
        continue

    if len(garbage_stack) > 0:
        garbage_char_count += 1
        continue

    if symbol == '{':
        if len(bracket_stack) > 0:
            level = bracket_stack[-1]+1
        else:
            level = 1
        bracket_stack.append(level)
        continue

    if symbol == '}':
        group_score += bracket_stack.pop()
        group_count += 1
        continue

print("There are %i groups" % group_count)
print("The total score is %i" % group_score)
print("There were %i characters in the garbage" % garbage_char_count)
