def solve_brute_force(numbers, target):
    n = len(numbers)
    solutions = []
    operations = 0  

    for i in range(n):
        for j in range(i+1, n):
            operations += 1

            if (numbers[i] + numbers[j]) == 9:
                solutions.append((numbers[i], numbers[j]))

    print(f"Search completed. Number of operations: {operations}")
    return solutions
