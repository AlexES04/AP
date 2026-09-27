def solve_brute_force(numbers, target):
    n = len(numbers)
    solutions = []
    operations = 0  

    for i in range(n):
        for j in range(i, n):
            operations += 1

            if (numbers[i] + numbers[j]) == target:
                solutions.append((numbers[i], numbers[j]))

    print(f"Search completed. \nTarget: {target}\nNumber of operations: {operations}")
    return solutions
