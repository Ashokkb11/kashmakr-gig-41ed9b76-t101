"""
Scientific Calculator Module

This module provides basic arithmetic and scientific calculation functions
with proper error handling and validation.
"""

import math
from typing import Union, Optional
from decimal import Decimal, InvalidOperation


class CalculatorError(Exception):
    """Custom exception for calculator errors."""
    pass


def validate_number(value: Union[int, float, str]) -> float:
    """
    Validate and convert input to float.
    
    Args:
        value: Input value to validate
        
    Returns:
        float: Validated float value
        
    Raises:
        CalculatorError: If value cannot be converted to float
    """
    if isinstance(value, (int, float)):
        return float(value)
    
    try:
        # Use Decimal for more precise string parsing
        return float(Decimal(str(value)))
    except (ValueError, InvalidOperation):
        raise CalculatorError(f"Invalid number: {value}")


def add(a: Union[int, float, str], b: Union[int, float, str]) -> float:
    """
    Add two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        float: Sum of a and b
    """
    a_val = validate_number(a)
    b_val = validate_number(b)
    return a_val + b_val


def subtract(a: Union[int, float, str], b: Union[int, float, str]) -> float:
    """
    Subtract b from a.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        float: Result of a - b
    """
    a_val = validate_number(a)
    b_val = validate_number(b)
    return a_val - b_val


def multiply(a: Union[int, float, str], b: Union[int, float, str]) -> float:
    """
    Multiply two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        float: Product of a and b
    """
    a_val = validate_number(a)
    b_val = validate_number(b)
    return a_val * b_val


def divide(a: Union[int, float, str], b: Union[int, float, str]) -> float:
    """
    Divide a by b.
    
    Args:
        a: Numerator
        b: Denominator
        
    Returns:
        float: Result of a / b
        
    Raises:
        CalculatorError: If b is zero
    """
    a_val = validate_number(a)
    b_val = validate_number(b)
    
    if abs(b_val) < 1e-15:  # Handle floating point precision
        raise CalculatorError("Division by zero is not allowed")
    
    return a_val / b_val


def power(base: Union[int, float, str], exponent: Union[int, float, str]) -> float:
    """
    Raise base to the power of exponent.
    
    Args:
        base: Base number
        exponent: Exponent
        
    Returns:
        float: base raised to exponent
        
    Raises:
        CalculatorError: For invalid operations like 0^negative
    """
    base_val = validate_number(base)
    exp_val = validate_number(exponent)
    
    # Handle edge cases
    if base_val == 0 and exp_val < 0:
        raise CalculatorError("Zero cannot be raised to a negative power")
    
    try:
        result = math.pow(base_val, exp_val)
        if math.isinf(result) or math.isnan(result):
            raise CalculatorError("Result is infinite or not a number")
        return result
    except ValueError as e:
        raise CalculatorError(f"Invalid power operation: {e}")


def sqrt(value: Union[int, float, str]) -> float:
    """
    Calculate square root of a number.
    
    Args:
        value: Number to calculate square root of
        
    Returns:
        float: Square root of value
        
    Raises:
        CalculatorError: If value is negative
    """
    val = validate_number(value)
    
    if val < 0:
        raise CalculatorError("Cannot calculate square root of negative number")
    
    return math.sqrt(val)


# Optional: Additional scientific functions could be added here
# For example: log, sin, cos, tan, etc.

if __name__ == "__main__":
    # Simple command-line interface for testing
    import sys
    
    if len(sys.argv) > 1:
        operation = sys.argv[1].lower()
        try:
            if operation == "add" and len(sys.argv) == 4:
                result = add(sys.argv[2], sys.argv[3])
                print(f"Result: {result}")
            elif operation == "subtract" and len(sys.argv) == 4:
                result = subtract(sys.argv[2], sys.argv[3])
                print(f"Result: {result}")
            elif operation == "multiply" and len(sys.argv) == 4:
                result = multiply(sys.argv[2], sys.argv[3])
                print(f"Result: {result}")
            elif operation == "divide" and len(sys.argv) == 4:
                result = divide(sys.argv[2], sys.argv[3])
                print(f"Result: {result}")
            elif operation == "power" and len(sys.argv) == 4:
                result = power(sys.argv[2], sys.argv[3])
                print(f"Result: {result}")
            elif operation == "sqrt" and len(sys.argv) == 3:
                result = sqrt(sys.argv[2])
                print(f"Result: {result}")
            else:
                print("Usage:")
                print("  python main.py add <a> <b>")
                print("  python main.py subtract <a> <b>")
                print("  python main.py multiply <a> <b>")
                print("  python main.py divide <a> <b>")
                print("  python main.py power <base> <exponent>")
                print("  python main.py sqrt <value>")
        except CalculatorError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
    else:
        print("Scientific Calculator Module")
        print("Available functions: add, subtract, multiply, divide, power, sqrt")