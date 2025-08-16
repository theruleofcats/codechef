t = int(input())

for i in range(t):
    line = input()
    earned, tax = line.split()
    invest = int(earned) - int(tax)
    print(invest)