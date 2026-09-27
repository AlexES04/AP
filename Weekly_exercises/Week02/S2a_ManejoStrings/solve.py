def solve(input_list):
    numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}

    result = 0

    for input in input_list:
        digits_founded = []
        for i in range(len(input)):
            for number in numbers:
                if input[i:].startswith(number):
                    digits_founded.append(numbers[number])
        result += digits_founded[0]*10+digits_founded[-1]
    return result
