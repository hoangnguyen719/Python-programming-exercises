import re
sentence = input('Sentence: ')

UPPER = re.findall(r'[A-Z]', sentence)
LOWER = re.findall(r'[a-z]', sentence)

print('Upper characters: {}'.format(len(UPPER)))
print('Lower characters: {}'.format(len(LOWER)))
