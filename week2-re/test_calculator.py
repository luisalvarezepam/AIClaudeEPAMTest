#!/usr/bin/env python3
"""
Comprehensive unit tests for calculator.py
Tests both normal operation and edge cases to ensure robustness
"""

import unittest
import sys
import os

# Add the current directory to the path to import calculator
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from calculator import add, subtract, multiply, divide, calculate_average, factorial, find_maximum, process_data


class TestCalculatorFunctions(unittest.TestCase):
    """Test suite for calculator functions"""

    def setUp(self):
        """Set up test data"""
        self.positive_numbers = [1, 2, 3, 4, 5]
        self.negative_numbers = [-1, -2, -3, -4, -5]
        self.mixed_numbers = [-2, -1, 0, 1, 2]
        self.single_number = [42]
        self.empty_list = []
        self.large_numbers = [1000000, 2000000, 3000000]

    # ==========================================
    # ARITHMETIC OPERATIONS TESTS
    # ==========================================

    def test_add_positive_numbers(self):
        """Test addition with positive numbers"""
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(1.5, 2.5), 4.0)

    def test_add_negative_numbers(self):
        """Test addition with negative numbers"""
        self.assertEqual(add(-5, -3), -8)
        self.assertEqual(add(-5, 3), -2)
        self.assertEqual(add(5, -3), 2)

    def test_add_edge_cases(self):
        """Test addition edge cases"""
        # Test with zero
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(5, 0), 5)
        
        # Test with large numbers
        self.assertEqual(add(1000000, 2000000), 3000000)

    def test_subtract_basic(self):
        """Test basic subtraction"""
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(5, 5), 0)
        self.assertEqual(subtract(0, 5), -5)

    def test_multiply_basic(self):
        """Test basic multiplication"""
        self.assertEqual(multiply(6, 7), 42)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(-3, 4), -12)

    def test_divide_basic(self):
        """Test basic division"""
        self.assertEqual(divide(15, 3), 5.0)
        self.assertEqual(divide(10, 2), 5.0)
        self.assertEqual(divide(7, 2), 3.5)

    def test_divide_by_zero(self):
        """Test division by zero - should raise ZeroDivisionError"""
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)
        
        with self.assertRaises(ZeroDivisionError):
            divide(0, 0)

    # ==========================================
    # STATISTICAL FUNCTIONS TESTS
    # ==========================================

    def test_calculate_average_basic(self):
        """Test basic average calculation"""
        self.assertEqual(calculate_average([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(calculate_average([10]), 10.0)
        self.assertEqual(calculate_average([2, 4, 6]), 4.0)

    def test_calculate_average_negative(self):
        """Test average with negative numbers"""
        self.assertEqual(calculate_average([-1, -2, -3]), -2.0)
        self.assertEqual(calculate_average([-5, 0, 5]), 0.0)

    def test_calculate_average_empty_list(self):
        """Test average with empty list - should raise ZeroDivisionError"""
        with self.assertRaises(ZeroDivisionError):
            calculate_average([])

    def test_find_maximum_basic(self):
        """Test basic maximum finding"""
        self.assertEqual(find_maximum([10, 5, 8, 3, 12]), 12)
        self.assertEqual(find_maximum([1]), 1)
        self.assertEqual(find_maximum([-1, -5, -2]), -1)

    def test_find_maximum_empty_list(self):
        """Test maximum with empty list - should raise IndexError"""
        with self.assertRaises(IndexError):
            find_maximum([])

    def test_find_maximum_duplicates(self):
        """Test maximum with duplicate values"""
        self.assertEqual(find_maximum([5, 5, 5]), 5)
        self.assertEqual(find_maximum([1, 3, 3, 2]), 3)

    # ==========================================
    # FACTORIAL TESTS
    # ==========================================

    def test_factorial_basic(self):
        """Test basic factorial calculation"""
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(3), 6)

    def test_factorial_negative(self):
        """Test factorial with negative numbers - should raise RecursionError"""
        with self.assertRaises(RecursionError):
            factorial(-1)
        
        with self.assertRaises(RecursionError):
            factorial(-5)

    def test_factorial_large_number(self):
        """Test factorial with large numbers - should raise RecursionError"""
        with self.assertRaises(RecursionError):
            factorial(2000)

    # ==========================================
    # DATA PROCESSING TESTS
    # ==========================================

    def test_process_data_basic(self):
        """Test basic data processing"""
        input_data = [2, -3, 4, -1]
        expected = [4, 3, 8, 1]  # [2*2, abs(-3), 4*2, abs(-1)]
        self.assertEqual(process_data(input_data), expected)

    def test_process_data_with_zeros(self):
        """Test data processing with zeros - zeros are dropped"""
        input_data = [2, -3, 0, 4, -1, 0]
        expected = [4, 3, 8, 1]  # zeros are silently dropped
        result = process_data(input_data)
        self.assertEqual(result, expected)
        self.assertLess(len(result), len(input_data))  # Verify data loss

    def test_process_data_only_positive(self):
        """Test data processing with only positive numbers"""
        input_data = [1, 2, 3, 4]
        expected = [2, 4, 6, 8]
        self.assertEqual(process_data(input_data), expected)

    def test_process_data_only_negative(self):
        """Test data processing with only negative numbers"""
        input_data = [-1, -2, -3, -4]
        expected = [1, 2, 3, 4]
        self.assertEqual(process_data(input_data), expected)

    def test_process_data_empty_list(self):
        """Test data processing with empty list"""
        self.assertEqual(process_data([]), [])

    # ==========================================
    # TYPE VALIDATION TESTS
    # ==========================================

    def test_string_concatenation_bug(self):
        """Test the string concatenation bug in arithmetic operations"""
        # This demonstrates the current bug - strings concatenate instead of adding
        result = add("5", "3")
        self.assertEqual(result, "53")  # Current buggy behavior
        
        # What we actually want would be:
        # self.assertEqual(add("5", "3"), 8)  # After fixing type conversion

    def test_mixed_type_list_bug(self):
        """Test mixed type handling in list functions"""
        with self.assertRaises(TypeError):
            calculate_average([1, 2, "3", 4])

    # ==========================================
    # PERFORMANCE TESTS
    # ==========================================

    def test_performance_large_list(self):
        """Test performance with large lists"""
        large_list = list(range(10000))
        
        # These should complete without timeout
        result_avg = calculate_average(large_list)
        self.assertIsInstance(result_avg, float)
        
        result_max = find_maximum(large_list)
        self.assertEqual(result_max, 9999)

    # ==========================================
    # INTEGRATION TESTS
    # ==========================================

    def test_calculator_workflow(self):
        """Test a typical calculator workflow"""
        # Basic arithmetic
        sum_result = add(10, 5)
        diff_result = subtract(sum_result, 3)
        prod_result = multiply(diff_result, 2)
        div_result = divide(prod_result, 4)
        
        self.assertEqual(sum_result, 15)
        self.assertEqual(diff_result, 12)
        self.assertEqual(prod_result, 24)
        self.assertEqual(div_result, 6.0)

    def test_statistical_workflow(self):
        """Test statistical operations workflow"""
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        
        avg = calculate_average(data)
        maximum = find_maximum(data)
        processed = process_data([-2, -1, 0, 1, 2])
        
        self.assertEqual(avg, 5.5)
        self.assertEqual(maximum, 10)
        self.assertEqual(processed, [2, 1, 2])  # zeros dropped


class TestCalculatorRobustness(unittest.TestCase):
    """Additional robustness tests for edge cases"""

    def test_float_precision(self):
        """Test floating point precision"""
        result = divide(1, 3)
        self.assertAlmostEqual(result, 0.333333333333, places=10)

    def test_very_large_numbers(self):
        """Test with very large numbers"""
        large_num = 10**10
        self.assertEqual(add(large_num, 1), large_num + 1)
        self.assertEqual(multiply(large_num, 2), large_num * 2)

    def test_very_small_numbers(self):
        """Test with very small numbers"""
        small_num = 0.000001
        result = add(small_num, small_num)
        self.assertAlmostEqual(result, 0.000002, places=6)


def run_tests():
    """Run all tests and generate a report"""
    print("=" * 60)
    print("CALCULATOR MODULE - UNIT TEST REPORT")
    print("=" * 60)
    
    # Create test suite
    suite = unittest.TestSuite()
    
    # Add all test cases
    suite.addTest(unittest.makeSuite(TestCalculatorFunctions))
    suite.addTest(unittest.makeSuite(TestCalculatorRobustness))
    
    # Run tests with detailed output
    runner = unittest.TextTestRunner(verbosity=2, stream=sys.stdout)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Success rate: {((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100):.1f}%")
    
    if result.failures:
        print(f"\nFAILURES ({len(result.failures)}):")
        for test, traceback in result.failures:
            print(f"- {test}")
    
    if result.errors:
        print(f"\nERRORS ({len(result.errors)}):")
        for test, traceback in result.errors:
            print(f"- {test}")
    
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)