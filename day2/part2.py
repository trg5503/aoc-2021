input = [x.strip() for x in open('input.txt').readlines()]

horiz, depth, aim = 0, 0, 0
for line in input:
    op, val = line.split(' ')
    if op == 'down':
        aim += int(val)
    elif op == 'up':
        aim -= int(val)
    elif op == 'forward':
        horiz += int(val)
        depth += aim * int(val)

total = horiz * depth
print(f'{horiz=}; {depth=}; {total=}')
