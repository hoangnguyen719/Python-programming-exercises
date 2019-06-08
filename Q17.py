logs = {'D':[], 'W':[]}
while True:
    try:
        action, amount = input('Transaction: ').split()
        logs[action].append(int(amount))
    except:
        break
print(sum(logs['D']) - sum(logs['W']))