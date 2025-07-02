#!/usr/bin/env python3
"""
Unit tests for the fixed calculator module
Tests all bug fixes and ensures proper functionality
"""

import unittest
import sys
import os

# Import the fixed calculator
from calculator_fixed import (
    add, subtract, multiply, divide, calculate_average, factorial, 
    find_maximum, process_data, CalculatorError, timed_execution,
    batch_calculate_average
)


class TestFixedCalculatorFunctions(unittest.TestCase):
    """Test suite for fixed calculator functions"""

    # ==========================================
    # ARITHMETIC OPERATIONS TESTS
    # ==========================================

    def test_add_fixed(self):
        """Test that string concatenation bug is fixed"""
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add("5", "3"), 8)  # Now properly converts and adds
        self.assertEqual(add("1.5", "2.5"), 4.0)
        self.assertEqual(add(-5, 3), -2)

    def test_add_type_validation(self):
        """Test type validation in add function"""
        with self.assertRaises(CalculatorError):
            add("abc", 5)
        
        with self.assertRaises(CalculatorError):
            add(5, [1, 2, 3])

    def test_divide_fixed(self):
        """Test that division by zero is properly handled"""
        self.assertEqual(divide(15, 3), 5.0)
        self.assertEqual(divide("10", "2"), 5.0)
        
        # Test division by zero handling
        with self.assertRaises(CalculatorError) as context:
            divide(10, 0)
        self.assertIn("Division by zero", str(context.exception))
        
        with self.assertRaises(CalculatorError):
            divide("10", "0")

    # ==========================================
    # STATISTICAL FUNCTIONS TESTS
    # ==========================================

    def test_calculate_average_fixed(self):
        """Test that empty list handling is fixed"""
        self.assertEqual(calculate_average([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(calculate_average(["1", "2", "3"]), 2.0)
        
        # Test empty list handling
        with self.assertRaises(CalculatorError) as context:
            calculate_average([])
        self.assertIn("cannot be an empty list", str(context.exception))
        
        # Test mixed type handling
        with self.assertRaises(CalculatorError):
            calculate_average([1, 2, "abc", 4])

    def test_find_maximum_fixed(self):
        """Test that empty list handling is fixed"""
        self.assertEqual(find_maximum([10, 5, 8, 3, 12]), 12)
        self.assertEqual(find_maximum(["10", "5", "8"]), 10)
        
        # Test empty list handling
        with self.assertRaises(CalculatorError) as context:
            find_maximum([])
        self.assertIn("cannot be an empty list", str(context.exception))

    # ==========================================
    # FACTORIAL TESTS
    # ==========================================

    def test_factorial_fixed(self):
        """Test that factorial bugs are fixed"""
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial("5"), 120)  # String conversion
        
        # Test negative number handling
        with self.assertRaises(CalculatorError) as context:
            factorial(-1)
        self.assertIn("not defined for negative", str(context.exception))
        
        # Test large number handling
        with self.assertRaises(CalculatorError) as context:
            factorial(2000)
        self.assertIn("too large", str(context.exception))
        
        # Test non-integer handling
        with self.assertRaises(CalculatorError):
            factorial(3.5)

    def test_factorial_performance(self):
        """Test factorial performance improvement"""
        # Large factorial should work with iterative approach
        result = factorial(100)
        self.assertIsInstance(result, int)
        self.assertGreater(result, 0)
        
        # Compare iterative vs recursive for smaller numbers
        result_iter = factorial(10, iterative=True)
        result_rec = factorial(10, iterative=False)
        self.assertEqual(result_iter, result_rec)

    # ==========================================
    # DATA PROCESSING TESTS
    # ==========================================

    def test_process_data_fixed(self):
        """Test that zero handling is properly implemented"""
        input_data = [2, -3, 0, 4, -1]
        
        # Test include zeros (default behavior)
        result_include = process_data(input_data, handle_zeros='include')
        expected_include = [4, 3, 0, 8, 1]
        self.assertEqual(result_include, expected_include)
        
        # Test drop zeros
        result_drop = process_data(input_data, handle_zeros='drop')
        expected_drop = [4, 3, 8, 1]
        self.assertEqual(result_drop, expected_drop)
        
        # Test with string inputs
        result_string = process_data(["2", "-3", "0"], handle_zeros='include')
        self.assertEqual(result_string, [4, 3, 0])

    def test_process_data_validation(self):
        """Test process_data input validation"""
        # Test invalid handle_zeros parameter
        with self.assertRaises(CalculatorError):
            process_data([1, 2, 3], handle_zeros='invalid')
        
        # Test non-list input
        with self.assertRaises(CalculatorError):
            process_data("not a list")
        
        # Test invalid numeric data
        with self.assertRaises(CalculatorError):
            process_data([1, 2, "abc"])

    # ==========================================
    # PERFORMANCE AND UTILITY TESTS
    # ==========================================

    def test_timed_execution(self):
        """Test the timing utility function"""
        result, time_ms = timed_execution(add, 5, 3)
        self.assertEqual(result, 8)
        self.assertIsInstance(time_ms, float)
        self.assertGreaterEqual(time_ms, 0)

    def test_batch_calculate_average(self):
        """Test batch average calculation"""
        lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        results = batch_calculate_average(lists)
        expected = [2.0, 5.0, 8.0]
        self.assertEqual(results, expected)
        
        # Test with invalid list
        with self.assertRaises(CalculatorError):
            batch_calculate_average([[1, 2, 3], []])

    # ==========================================
    # INTEGRATION TESTS
    # ==========================================

    def test_full_workflow_fixed(self):
        """Test that all functions work together without errors"""
        # Arithmetic operations with type conversion
        a = add("10", "5")
        b = subtract(a, 3)
        c = multiply(b, 2)
        d = divide(c, 4)
        
        self.assertEqual(a, 15)
        self.assertEqual(b, 12)
        self.assertEqual(c, 24)
        self.assertEqual(d, 6.0)
        
        # Statistical operations
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        avg = calculate_average(data)
        maximum = find_maximum(data)
        
        self.assertEqual(avg, 5.5)
        self.assertEqual(maximum, 10)
        
        # Data processing with explicit zero handling
        processed_include = process_data([-2, -1, 0, 1, 2], 'include')
        processed_drop = process_data([-2, -1, 0, 1, 2], 'drop')
        
        self.assertEqual(processed_include, [2, 1, 0, 2, 4])
        self.assertEqual(processed_drop, [2, 1, 2, 4])
        
        # Factorial
        fact = factorial(6)
        self.assertEqual(fact, 720)

    def test_error_messages(self):
        """Test that error messages are informative"""
        try:
            divide(10, 0)
        except CalculatorError as e:
            self.assertIn("Division by zero", str(e))
        
        try:
            calculate_average([])
        except CalculatorError as e:
            self.assertIn("empty list", str(e))
        
        try:
            factorial(-1)
        except CalculatorError as e:
            self.assertIn("negative", str(e))


class TestPerformanceImprovements(unittest.TestCase):
    """Test performance improvements in the fixed version"""

    def test_large_list_performance(self):
        """Test that large lists are handled efficiently"""
        large_list = list(range(50000))
        
        # These should complete quickly without errors
        result, time_ms = timed_execution(calculate_average, large_list)
        self.assertLess(time_ms, 100)  # Should complete in under 100ms
        
        result, time_ms = timed_execution(find_maximum, large_list)
        self.assertLess(time_ms, 100)  # Should complete in under 100ms

    def test_factorial_performance(self):
        """Test that factorial is much faster with iterative approach"""
        # Test iterative vs recursive performance
        result_iter, time_iter = timed_execution(factorial, 50, iterative=True)
        result_rec, time_rec = timed_execution(factorial, 50, iterative=False)
        
        self.assertEqual(result_iter, result_rec)
        # Iterative should be faster or at least not significantly slower
        self.assertLessEqual(time_iter, time_rec * 2)


def run_fixed_tests():
    """Run all tests for the fixed calculator"""
    print("=" * 60)
    print("FIXED CALCULATOR MODULE - COMPREHENSIVE TEST REPORT")
    print("=" * 60)
    
    # Create test suite
    suite = unittest.TestSuite()
    
    # Add all test cases
    suite.addTest(unittest.makeSuite(TestFixedCalculatorFunctions))
    suite.addTest(unittest.makeSuite(TestPerformanceImprovements))
    
    # Run tests with detailed output
    runner = unittest.TextTestRunner(verbosity=2, stream=sys.stdout)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "=" * 60)
    print("FIXED VERSION TEST SUMMARY")
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
    
    print("\n" + "=" * 60)
    if result.wasSuccessful():
        print("🎉 ALL TESTS PASSED! All bugs have been successfully fixed!")
    else:
        print("❌ Some tests failed. Further debugging needed.")
    print("=" * 60)
    
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_fixed_tests()
    sys.exit(0 if success else 1)