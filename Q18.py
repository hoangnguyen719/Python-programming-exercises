import re
passwords = []
options = input('What are possible passwords: ').split(',')

for possible in options:
    if (len(possible) >= 6) & (len(possible) <= 12):
        if re.search(r'[a-z]', possible):
            if re.search(r'[A-Z]', possible):
                if re.search(r'[0-9]', possible):
                    if re.search(r'[\$#@]', possible):
                        passwords.append(possible)
print(*passwords, sep = ',')