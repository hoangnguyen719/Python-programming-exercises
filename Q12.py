evens = ['0', '2', '4', '6', '8']
result = [['2', x, y, z] for x in evens for y in evens for z in evens]

print(*map(int, [''.join(x) for x in result]), sep=',')