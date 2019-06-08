a = input('What is a: ')
max_a = input('What is characters in aaa...a: ')
print(sum(map(int, [a*i for i in range(1, int(max_a) + 1)])))
