input = [x.strip() for x in open('input.txt').readlines()]

common_bits = []
for i in range(len(input[0])):
    this_bit = []
    for line in input:
        bit = line[i]
        this_bit.append(bit)
    ones, zeros = this_bit.count('1'), this_bit.count('0')
    common_bits.append([ones, zeros])

gamma, epsilon = '', ''
for ones, zeros in common_bits:
    if ones > zeros:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

print(f'{gamma=} * {epsilon=} = {int(gamma,2) * int(epsilon,2)}')