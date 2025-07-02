def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def find_maximum(numbers):
    max_val = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] > max_val:
            max_val = numbers[i]
    return max_val

def process_data(data_list):
    results = []
    for item in data_list:
        if item > 0:
            results.append(item * 2)
        elif item < 0:
            results.append(abs(item))
    return results

if __name__ == "__main__":
    print("Calculator Test")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"6 * 7 = {multiply(6, 7)}")
    print(f"15 / 3 = {divide(15, 3)}")
    
    nums = [1, 2, 3, 4, 5]
    print(f"Average of {nums} = {calculate_average(nums)}")
    
    print(f"Factorial of 5 = {factorial(5)}")
    
    test_nums = [10, 5, 8, 3, 12]
    print(f"Maximum of {test_nums} = {find_maximum(test_nums)}")
    
    test_data = [2, -3, 0, 4, -1]
    print(f"Processed data: {process_data(test_data)}")