input = [[y.split() for y in x.split(' | ')] for x in open('input.txt').readlines()]

digit_map = {
    2: '1',
    4: '4',
    3: '7',
    7: '8'
}

found = []
for pattern, output in input:
    for x in output:
        try:
            found += digit_map[len(x)]
        except KeyError:
            pass

print(len(found))