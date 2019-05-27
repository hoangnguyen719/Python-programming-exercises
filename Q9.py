lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break

print(*[l.upper() for l in lines], sep='\n')