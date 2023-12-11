
def find_first_last_occurrences(line):
    numbers = []
    for char in line:
        if char.isdigit():
            numbers.append(int(char))
    if len(numbers) == 1:
        return numbers[0] * 11
    elif numbers:
        return (numbers[0] * 10) + numbers[-1]
    else:
        return None

def calculate_sum_of_occurrences(file_path):
    total_sum = 0
    with open(file_path, 'r') as file:
        for line in file:
            first_and_last = find_first_last_occurrences(line)
            if first_and_last is not None:
                total_sum += first_and_last
    return total_sum

file_path = input("Enter the file path: ")
sum_of_occurrences = calculate_sum_of_occurrences(file_path)
print("Sum of first and last occurrences:", sum_of_occurrences)
