X, Y = map(int, input('Two digits: ').split(','))
result = []
for i in range(0,X):
    new = []
    for j in range(0,Y):
        new.append(i*j)
    result.append(new)

print(result)