import statistics
input = [int(x) for x in open('input.txt').read().split(',')]

best = int(statistics.median_grouped(input))

moves = 0
for i in input:
    moves += abs(best - i)

print(moves)