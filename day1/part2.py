input = [int(x) for x in open('input.txt').readlines()]

last, result = sum(input[0:3]), 0
for i in range(1, len(input) - 2):
    current = sum(input[i:i+3])
    if current > last:
        result += 1
    last = current

print(result)