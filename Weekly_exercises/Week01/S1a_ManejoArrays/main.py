from solve_tsp import *

test_file = "test.txt"

if test_file is not None:
    input_source = open(test_file, 'r', newline='')
else:
    import sys
    input_source = sys.stdin
# ----------------------------------------------------------------

string1 = input_source.readline()
parent1 = [int(k) for k in string1.split(',')]

string2 = input_source.readline()
parent2 = [int(k) for k in string2.split(',')]

lower_bound = int(input_source.readline())
upper_bound = int(input_source.readline())

solution = order_crossover(parent1, parent2, lower_bound, upper_bound)

print(solution)

# --------------------------------------------------------------------
# Close the file if it was opened
if test_file is not None:
    input_source.close()