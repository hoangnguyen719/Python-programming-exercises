C = 50
H = 30
D = list(map(int, input('Comma-separated sequence: ').split(',')))

print(*[round((2*C*i/H)**(1/2)) for i in D], sep=',')
