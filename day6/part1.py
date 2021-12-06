import numpy as np
input = [int(x) for x in open('input.txt').read().split(',')]

fish = np.array([*input])

print('Initial state:', fish)
target_days = 80
day = 1
while day <= target_days:
    fish = fish - 1
    day_new_fish = 0
    for i in np.arange(len(fish)):
        if fish[i] == -1:
            fish[i] = 6
            day_new_fish += 1
    fish = np.append(fish, [8] * day_new_fish)
    print(f'After {day:>2} days: {len(fish)}')
    day += 1