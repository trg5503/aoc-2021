input = [x.strip() for x in open('input.txt').readlines()]

horiz, depth = 0, 0
for line in input:
    op, val = line.split(' ')
    if op == 'forward':
        horiz += int(val)
    elif op == 'down':
        depth += int(val)
    elif op == 'up':
        depth -= int(val)

total = horiz * depth
print(f'{horiz=}; {depth=}; {total=}')
