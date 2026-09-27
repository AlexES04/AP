def solve(input_list):
    instruction_count = {"N": 0, "E": 0,  "S": 0, "W": 0}
    orientations = {"N": ["W", "E"], "E": ["N", "S"], "S": ["E", "W"], "W": ["S", "N"]}
    orientation = "N"

    for instruction in input_list:
        if instruction[0] == "R":
            orientation = orientations[orientation][0]
        else:
            orientation = orientations[orientation][1]
        instruction_count[orientation] += int(instruction[1:])

    y_distance = abs(instruction_count["N"] - instruction_count["S"])
    x_distance = abs(instruction_count["E"] - instruction_count["W"])
    return (x_distance + y_distance)