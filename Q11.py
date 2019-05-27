numbers = input('Comma-separated binary numbers: ').split(',')

result = []
for number in numbers:
    if (int(number, 2) % 5) == 0:
        result.append(number)

print(*result)