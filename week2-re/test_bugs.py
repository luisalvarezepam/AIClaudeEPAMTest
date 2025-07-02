#!/usr/bin/env python3
"""
Bug detection script for calculator.py
Tests various edge cases to identify potential issues
"""

from calculator import *

def test_edge_cases():
    print("=== BUG DETECTION TESTS ===")
    
    # Test 1: Division by zero
    print("\n1. Testing division by zero:")
    try:
        result = divide(10, 0)
        print(f"divide(10, 0) = {result}")
    except Exception as e:
        print(f"ERROR: {type(e).__name__}: {e}")
    
    # Test 2: Empty list in calculate_average
    print("\n2. Testing empty list in calculate_average:")
    try:
        result = calculate_average([])
        print(f"calculate_average([]) = {result}")
    except Exception as e:
        print(f"ERROR: {type(e).__name__}: {e}")
    
    # Test 3: Empty list in find_maximum
    print("\n3. Testing empty list in find_maximum:")
    try:
        result = find_maximum([])
        print(f"find_maximum([]) = {result}")
    except Exception as e:
        print(f"ERROR: {type(e).__name__}: {e}")
    
    # Test 4: Negative number in factorial
    print("\n4. Testing negative number in factorial:")
    try:
        result = factorial(-5)
        print(f"factorial(-5) = {result}")
    except Exception as e:
        print(f"ERROR: {type(e).__name__}: {e}")
    
    # Test 5: Large number in factorial (stack overflow risk)
    print("\n5. Testing large number in factorial:")
    try:
        result = factorial(2000)  # This might cause stack overflow
        print(f"factorial(2000) = {result}")
    except Exception as e:
        print(f"ERROR: {type(e).__name__}: {e}")
    
    # Test 6: process_data with zero handling
    print("\n6. Testing process_data with zeros:")
    test_data = [2, -3, 0, 4, -1, 0, 5]
    result = process_data(test_data)
    print(f"process_data({test_data}) = {result}")
    print(f"Original length: {len(test_data)}, Result length: {len(result)}")
    print("Note: Zero values are silently dropped!")
    
    # Test 7: String inputs (type checking)
    print("\n7. Testing string inputs:")
    try:
        result = add("5", "3")
        print(f"add('5', '3') = {result}")
    except Exception as e:
        print(f"ERROR: {type(e).__name__}: {e}")
    
    # Test 8: Mixed types in lists
    print("\n8. Testing mixed types in calculate_average:")
    try:
        result = calculate_average([1, 2, "3", 4, 5])
        print(f"calculate_average([1, 2, '3', 4, 5]) = {result}")
    except Exception as e:
        print(f"ERROR: {type(e).__name__}: {e}")

if __name__ == "__main__":
    test_edge_cases()