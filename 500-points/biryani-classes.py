t = int(input())

for i in range(t):
    line = input()
    x, y = line.split()
    cost = int(x) * int(y)
    print(cost)