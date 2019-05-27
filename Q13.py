import re
sentence = input('Sentence: ')
num = re.findall(r'\d', sentence)
char = re.findall(r'[a-zA-Z]', sentence)

print('LETTERS {}'.format(len(char)))
print('DIGITs {}'.format(len(num)))
