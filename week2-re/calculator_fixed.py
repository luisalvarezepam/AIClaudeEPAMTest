#!/usr/bin/env python3
"""
Fixed Calculator Module - All bugs resolved
===========================================

This module provides robust mathematical utility functions with proper
error handling, input validation, and performance optimizations.

Author: Claude AI (Bug Fix Version)
Date: 2025-07-02
Version: 2.0 (Fixed)
"""

import time
from typing import List, Union, Optional


class CalculatorError(Exception):
    """Custom exception for calculator-specific errors"""
    pass


def validate_numeric_input(value, param_name: str) -> Union[int, float]:
    """
    Validate that input is numeric and convert if necessary
    
    Args:
        value: Input value to validate
        param_name: Name of parameter for error messages
        
    Returns:
        Numeric value (int or float)
        
    Raises:
        CalculatorError: If input is not numeric
    """
    if isinstance(value, (int, float)):
        return value
    elif isinstance(value, str):
        try:
            # Try to convert string to number
            if '.' in value:
                return float(value)
            else:
                return int(value)
        except ValueError:
            raise CalculatorError(f"Parameter '{param_name}' must be numeric, got '{value}'")
    else:
        raise CalculatorError(f"Parameter '{param_name}' must be numeric, got {type(value).__name__}")


def validate_numeric_list(numbers: List, param_name: str) -> List[Union[int, float]]:
    """
    Validate that all items in list are numeric
    
    Args:
        numbers: List to validate
        param_name: Name of parameter for error messages
        
    Returns:
        List of numeric values
        
    Raises:
        CalculatorError: If any item is not numeric or list is empty
    """
    if not isinstance(numbers, list):
        raise CalculatorError(f"Parameter '{param_name}' must be a list, got {type(numbers).__name__}")
    
    if len(numbers) == 0:
        raise CalculatorError(f"Parameter '{param_name}' cannot be an empty list")
    
    validated_numbers = []
    for i, num in enumerate(numbers):
        try:
            validated_numbers.append(validate_numeric_input(num, f"{param_name}[{i}]"))
        except CalculatorError as e:
            raise CalculatorError(f"Invalid item at index {i} in {param_name}: {str(e)}")
    
    return validated_numbers


# ==========================================
# BASIC ARITHMETIC OPERATIONS (FIXED)
# ==========================================

def add(a: Union[int, float, str], b: Union[int, float, str]) -> Union[int, float]:
    """
    Add two numbers with input validation
    
    Args:
        a: First number (numeric value or string representation)
        b: Second number (numeric value or string representation)
        
    Returns:
        Sum of a and b
        
    Raises:
        CalculatorError: If inputs are not numeric
        
    Examples:
        >>> add(5, 3)
        8
        >>> add("5", "3")
        8
        >>> add(1.5, 2.5)
        4.0
    """
    a_val = validate_numeric_input(a, 'a')
    b_val = validate_numeric_input(b, 'b')
    return a_val + b_val


def subtract(a: Union[int, float, str], b: Union[int, float, str]) -> Union[int, float]:
    """
    Subtract two numbers with input validation
    
    Args:
        a: Minuend (numeric value or string representation)
        b: Subtrahend (numeric value or string representation)
        
    Returns:
        Difference (a - b)
        
    Raises:
        CalculatorError: If inputs are not numeric
    """
    a_val = validate_numeric_input(a, 'a')
    b_val = validate_numeric_input(b, 'b')
    return a_val - b_val


def multiply(a: Union[int, float, str], b: Union[int, float, str]) -> Union[int, float]:
    """
    Multiply two numbers with input validation
    
    Args:
        a: First factor (numeric value or string representation)
        b: Second factor (numeric value or string representation)
        
    Returns:
        Product of a and b
        
    Raises:
        CalculatorError: If inputs are not numeric
    """
    a_val = validate_numeric_input(a, 'a')
    b_val = validate_numeric_input(b, 'b')
    return a_val * b_val


def divide(a: Union[int, float, str], b: Union[int, float, str]) -> float:
    """
    Divide two numbers with input validation and zero-division protection
    
    Args:
        a: Dividend (numeric value or string representation)
        b: Divisor (numeric value or string representation)
        
    Returns:
        Quotient (a / b)
        
    Raises:
        CalculatorError: If inputs are not numeric or if divisor is zero
    """
    a_val = validate_numeric_input(a, 'a')
    b_val = validate_numeric_input(b, 'b')
    
    if b_val == 0:
        raise CalculatorError("Division by zero is not allowed")
    
    return a_val / b_val


# ==========================================
# STATISTICAL FUNCTIONS (FIXED)
# ==========================================

def calculate_average(numbers: List[Union[int, float, str]]) -> float:
    """
    Calculate arithmetic mean with input validation and performance optimization
    
    Args:
        numbers: List of numeric values
        
    Returns:
        Average value as float
        
    Raises:
        CalculatorError: If list is empty or contains non-numeric values
        
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    validated_numbers = validate_numeric_list(numbers, 'numbers')
    
    # Use built-in sum() for better performance
    total = sum(validated_numbers)
    return total / len(validated_numbers)


def find_maximum(numbers: List[Union[int, float, str]]) -> Union[int, float]:
    """
    Find maximum value with input validation and performance optimization
    
    Args:
        numbers: List of numeric values
        
    Returns:
        Maximum value from the list
        
    Raises:
        CalculatorError: If list is empty or contains non-numeric values
        
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    validated_numbers = validate_numeric_list(numbers, 'numbers')
    
    # Use built-in max() for better performance
    return max(validated_numbers)


# ==========================================
# ADVANCED MATHEMATICAL FUNCTIONS (FIXED)
# ==========================================

def factorial(n: Union[int, str], iterative: bool = True) -> int:
    """
    Calculate factorial with input validation and iterative implementation
    
    Args:
        n: Non-negative integer
        iterative: Use iterative implementation (default) vs recursive
        
    Returns:
        Factorial of n (n!)
        
    Raises:
        CalculatorError: If n is negative or not an integer
        
    Time Complexity: O(n)
    Space Complexity: O(1) for iterative, O(n) for recursive
    """
    n_val = validate_numeric_input(n, 'n')
    
    # Ensure n is an integer
    if not isinstance(n_val, int) and not n_val.is_integer():
        raise CalculatorError("Factorial is only defined for integers")
    
    n_int = int(n_val)
    
    if n_int < 0:
        raise CalculatorError("Factorial is not defined for negative numbers")
    
    if n_int > 1000:  # Prevent extremely large computations
        raise CalculatorError("Factorial input too large (max 1000)")
    
    if iterative:
        # Iterative implementation - faster and no stack overflow risk
        result = 1
        for i in range(1, n_int + 1):
            result *= i
        return result
    else:
        # Recursive implementation (kept for comparison)
        if n_int == 0:
            return 1
        else:
            return n_int * factorial(n_int - 1, iterative=False)


# ==========================================
# DATA PROCESSING FUNCTIONS (FIXED)
# ==========================================

def process_data(data_list: List[Union[int, float, str]], handle_zeros: str = 'include') -> List[Union[int, float]]:
    """
    Process list of numbers with explicit zero handling
    
    Args:
        data_list: List of numeric values
        handle_zeros: How to handle zeros ('include', 'drop', 'double')
        
    Returns:
        Processed list based on conditions
        
    Processing Rules:
        - Positive numbers: multiply by 2
        - Negative numbers: return absolute value
        - Zero: based on handle_zeros parameter
        
    Raises:
        CalculatorError: If input validation fails
        
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if not isinstance(data_list, list):
        raise CalculatorError("Input must be a list")
    
    if len(data_list) == 0:
        return []
    
    if handle_zeros not in ['include', 'drop', 'double']:
        raise CalculatorError("handle_zeros must be 'include', 'drop', or 'double'")
    
    results = []
    for i, item in enumerate(data_list):
        try:
            num = validate_numeric_input(item, f"data_list[{i}]")
            
            if num > 0:
                results.append(num * 2)
            elif num < 0:
                results.append(abs(num))
            else:  # num == 0
                if handle_zeros == 'include':
                    results.append(0)
                elif handle_zeros == 'drop':
                    continue  # Skip zeros
                elif handle_zeros == 'double':
                    results.append(0)  # Could be 0 * 2 = 0
        except CalculatorError as e:
            raise CalculatorError(f"Error processing item at index {i}: {str(e)}")
    
    return results


# ==========================================
# PERFORMANCE OPTIMIZED UTILITIES
# ==========================================

def timed_execution(func, *args, **kwargs):
    """
    Measure execution time of a function
    
    Args:
        func: Function to execute
        *args: Function arguments
        **kwargs: Function keyword arguments
        
    Returns:
        Tuple of (result, execution_time_ms)
    """
    start_time = time.perf_counter()
    result = func(*args, **kwargs)
    end_time = time.perf_counter()
    execution_time_ms = (end_time - start_time) * 1000
    return result, execution_time_ms


def batch_calculate_average(list_of_lists: List[List[Union[int, float]]]) -> List[float]:
    """
    Calculate averages for multiple lists efficiently
    
    Args:
        list_of_lists: List containing multiple lists of numbers
        
    Returns:
        List of average values
        
    Raises:
        CalculatorError: If any list is invalid
    """
    results = []
    for i, numbers in enumerate(list_of_lists):
        try:
            avg = calculate_average(numbers)
            results.append(avg)
        except CalculatorError as e:
            raise CalculatorError(f"Error in list {i}: {str(e)}")
    return results


# ==========================================
# MAIN EXECUTION AND TESTING
# ==========================================

def demonstrate_fixes():
    """Demonstrate that all bugs have been fixed"""
    print("=" * 60)
    print("CALCULATOR MODULE - BUG FIXES DEMONSTRATION")
    print("=" * 60)
    
    # Test basic operations
    print("\n1. Basic Arithmetic (with type conversion):")
    print(f"add(5, 3) = {add(5, 3)}")
    print(f"add('5', '3') = {add('5', '3')}")  # Fixed: now returns 8, not '53'
    print(f"subtract(10, 4) = {subtract(10, 4)}")
    print(f"multiply(6, 7) = {multiply(6, 7)}")
    print(f"divide(15, 3) = {divide(15, 3)}")
    
    # Test fixed division by zero
    print("\n2. Division by Zero (Fixed):")
    try:
        result = divide(10, 0)
        print(f"divide(10, 0) = {result}")
    except CalculatorError as e:
        print(f"✓ Properly handled: {e}")
    
    # Test fixed empty list handling
    print("\n3. Empty List Handling (Fixed):")
    try:
        result = calculate_average([])
        print(f"calculate_average([]) = {result}")
    except CalculatorError as e:
        print(f"✓ Properly handled: {e}")
    
    try:
        result = find_maximum([])
        print(f"find_maximum([]) = {result}")
    except CalculatorError as e:
        print(f"✓ Properly handled: {e}")
    
    # Test fixed factorial
    print("\n4. Factorial Issues (Fixed):")
    print(f"factorial(5) = {factorial(5)}")
    
    try:
        result = factorial(-5)
        print(f"factorial(-5) = {result}")
    except CalculatorError as e:
        print(f"✓ Properly handled: {e}")
    
    # Test with large number (iterative approach)
    result, time_ms = timed_execution(factorial, 100)
    print(f"factorial(100) = {result} (computed in {time_ms:.2f}ms)")
    
    # Test fixed process_data with explicit zero handling
    print("\n5. Process Data with Zero Handling (Fixed):")
    test_data = [2, -3, 0, 4, -1, 0, 5]
    
    result_include = process_data(test_data, handle_zeros='include')
    print(f"process_data({test_data}, 'include') = {result_include}")
    
    result_drop = process_data(test_data, handle_zeros='drop')
    print(f"process_data({test_data}, 'drop') = {result_drop}")
    
    # Test statistical functions
    print("\n6. Statistical Functions:")
    nums = [1, 2, 3, 4, 5]
    print(f"calculate_average({nums}) = {calculate_average(nums)}")
    
    test_nums = [10, 5, 8, 3, 12]
    print(f"find_maximum({test_nums}) = {find_maximum(test_nums)}")
    
    # Performance comparison
    print("\n7. Performance Improvements:")
    large_list = list(range(1, 10001))
    
    # Test average calculation
    result, time_ms = timed_execution(calculate_average, large_list)
    print(f"calculate_average({len(large_list)} items) = {result:.2f} (in {time_ms:.2f}ms)")
    
    # Test maximum finding
    result, time_ms = timed_execution(find_maximum, large_list)
    print(f"find_maximum({len(large_list)} items) = {result} (in {time_ms:.2f}ms)")


if __name__ == "__main__":
    demonstrate_fixes()