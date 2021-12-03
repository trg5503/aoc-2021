input = [x.strip() for x in open('input.txt').readlines()]

def count_common_bits(bits):
    return bits.count('1'), bits.count('0')

def crit_most_common(bits):
    ones, zeros = count_common_bits(bits)
    return '1' if ones == zeros else '1' if ones > zeros else '0'

def crit_least_common(bits):
    ones, zeros = count_common_bits(bits)
    return '0' if ones == zeros else '0' if ones > zeros else '1'

def search(lines, criteria):
    filtered = [*lines]
    # i = index of bit we're searching
    for i in range(len(lines[0])):
        if len(filtered) == 1:
            break
        expected = criteria([line[i] for line in filtered])
        #print(f'found_common_bit={expected}')
        filtered = [x for x in filtered if x[i] == expected]
    #print(f'search complete with {criteria=} -- {filtered=}')
    return filtered[0]

oxygen = search(input, crit_most_common)
co2 = search(input, crit_least_common)

print(f'{oxygen=} ({int(oxygen,2)}) * {co2=} ({int(co2,2)}) = {int(oxygen,2) * int(co2,2)}')