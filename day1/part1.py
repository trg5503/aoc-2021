input = [int(x) for x in open('input.txt').readlines()]

last, result = input[0], 0
for current in input[1:]:
    if current > last:
        result += 1
    last = current

print(result)