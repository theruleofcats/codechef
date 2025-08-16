t = int(input())

for i in range(t):
    input_vals = input()
    points, test_cases = input_vals.split()
    
    points = int(points)
    test_cases = int(test_cases)
    
    single_case = points / 10
    score = single_case * test_cases
    
    print(int(score))