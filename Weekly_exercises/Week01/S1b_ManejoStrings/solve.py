def solve(input_list):

    result = 0
    for word in input_list:
        sum = 0
        digits = [character for character in word if character.isdigit()]
        if digits:
            sum = int(digits[0]+digits[-1])
        result += sum
    return result