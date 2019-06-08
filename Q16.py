l = list(map(int, input('List of number: ').split(',')))
print(*[i**2 for i in l if i%2==1], sep=',')