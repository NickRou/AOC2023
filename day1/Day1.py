digits_dict = {
    'one' : '1',
    'two' : '2',
    'three' : '3',
    'four' : '4',
    'five' : '5',
    'six' : '6',
    'seven' : '7',
    'eight' : '8',
    'nine' : '9',
}

def get_input_file_lines(file_name): 
    file = open(file_name, 'r')
    return file.readlines()

def get_first_digit(line):
    digit_str = ''
    for i in range(len(line)):
        if line[i].isdigit(): 
            return line[i]
        else: 
            digit_str += line[i]
            for digit in digits_dict: 
                if digit in digit_str: 
                    return digits_dict[digit]
    return ''

def get_last_digit(line):
    digit_str = ''
    for i in range(len(line)-1, -1, -1):
        if (line[i].isdigit()):
            return line[i]
        else: 
            digit_str = line[i] + digit_str
            for digit in digits_dict: 
                if digit in digit_str: 
                    return digits_dict[digit]
    return ''

def calculate_calibration_result(lines):
    calibration_result = 0
    for line in lines: 
        first_digit = get_first_digit(line)
        last_digit = get_last_digit(line)
        print("First Digit: " + first_digit + ", Last Digit: " + last_digit)
        two_digit_number = first_digit + last_digit
        calibration_result += int(two_digit_number)
    return calibration_result

def main():
    lines = get_input_file_lines('day1/puzzle_input.txt')
    calibration_result = calculate_calibration_result(lines)
    print(f'Calibration Results Sum: {calibration_result}')

if __name__ == "__main__":
    main()


