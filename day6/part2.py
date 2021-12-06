import numpy as np
input = [int(x) for x in open('input.txt').read().split(',')]

fish = {}

for i in range(9):
    fish[i] = input.count(i)

print('Initial state:', fish)
target_days = 256
day = 1
while day <= target_days:
    fish[0], fish[1], fish[2], fish[3], fish[4], fish[5], fish[6], fish[7], fish[8] = fish[1], fish[2], fish[3], fish[4], fish[5], fish[6], fish[7] + fish[0], fish[8], fish[0]
    print(f'After {day:>2} days: {sum(fish.values())}')
    day += 1