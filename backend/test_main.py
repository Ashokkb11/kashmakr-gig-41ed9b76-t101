import pytest
import main


def test_module_smoke():
    """Test that the module can be imported and has expected functions."""
    # Test that module has expected functions
    assert hasattr(main, 'add')
    assert hasattr(main, 'subtract')
    assert hasattr(main, 'multiply')
    assert hasattr(main, 'divide')
    assert hasattr(main, 'power')
    assert hasattr(main, 'sqrt')
    assert hasattr(main, 'CalculatorError')
    assert hasattr(main, 'validate_number')


def test_add():
    """Test addition function."""
    # Test basic addition
    assert main.add(2, 3) == 5.0
    assert main.add(-2, 3) == 1.0
    assert main.add(0, 0) == 0.0
    
    # Test with string inputs
    assert main.add("2.5", "3.5") == 6.0
    assert main.add(2.5, "3.5") == 6.0
    
    # Test with float inputs
    assert main.add(2.5, 3.5) == 6.0


def test_subtract():
    """Test subtraction function."""
    # Test basic subtraction
    assert main.subtract(5, 3) == 2.0
    assert main.subtract(3, 5) == -2.0
    assert main.subtract(0, 0) == 0.0
    
    # Test with string inputs
    assert main.subtract("5.5", "2.5") == 3.0
    assert main.subtract(5.5, "2.5") == 3.0


def test_multiply():
    """Test multiplication function."""
    # Test basic multiplication
    assert main.multiply(2, 3) == 6.0
    assert main.multiply(-2, 3) == -6.0
    assert main.multiply(0, 5) == 0.0
    
    # Test with string inputs
    assert main.multiply("2.5", "2") == 5.0
    assert main.multiply(2.5, "2") == 5.0


def test_divide():
    """Test division function."""
    # Test basic division
    assert main.divide(6, 3) == 2.0
    assert main.divide(5, 2) == 2.5
    assert main.divide(0, 5) == 0.0
    
    # Test with string inputs
    assert main.divide("6.0", "2.0") == 3.0
    assert main.divide(6.0, "2.0") == 3.0
    
    # Test division by zero raises CalculatorError
    with pytest.raises(main.CalculatorError, match="Division by zero is not allowed"):
        main.divide(5, 0)
    
    with pytest.raises(main.CalculatorError, match="Division by zero is not allowed"):
        main.divide(5, "0")


def test_power():
    """Test power function."""
    # Test basic power operations
    assert main.power(2, 3) == 8.0
    assert main.power(4, 0.5) == 2.0  # square root
    assert main.power(2, -1) == 0.5
    
    # Test with string inputs
    assert main.power("2", "3") == 8.0
    assert main.power(2, "3") == 8.0
    
    # Test edge case: 0 to negative power
    with pytest.raises(main.CalculatorError, match="Zero cannot be raised to a negative power"):
        main.power(0, -2)
    
    with pytest.raises(main.CalculatorError, match="Zero cannot be raised to a negative power"):
        main.power("0", "-2")


def test_sqrt():
    """Test square root function."""
    # Test basic square roots
    assert main.sqrt(4) == 2.0
    assert main.sqrt(9) == 3.0
    assert main.sqrt(0) == 0.0
    
    # Test with string inputs
    assert main.sqrt("4") == 2.0
    assert main.sqrt("9.0") == 3.0
    
    # Test negative input raises CalculatorError
    with pytest.raises(main.CalculatorError, match="Cannot calculate square root of negative number"):
        main.sqrt(-4)
    
    with pytest.raises(main.CalculatorError, match="Cannot calculate square root of negative number"):
        main.sqrt("-4")


def test_validate_number():
    """Test number validation function."""
    # Test valid inputs
    assert main.validate_number(5) == 5.0
    assert main.validate_number(3.14) == 3.14
    assert main.validate_number("5") == 5.0
    assert main.validate_number("3.14") == 3.14
    assert main.validate_number("-2.5") == -2.5
    
    # Test invalid inputs raise CalculatorError
    with pytest.raises(main.CalculatorError):
        main.validate_number("not a number")
    
    with pytest.raises(main.CalculatorError):
        main.validate_number("")


def test_calculator_error():
    """Test custom exception."""
    # Test that CalculatorError is a subclass of Exception
    assert issubclass(main.CalculatorError, Exception)
    
    # Test that we can raise and catch it
    try:
        raise main.CalculatorError("Test error")
    except main.CalculatorError as e:
        assert str(e) == "Test error"


def test_integration():
    """Test integration of multiple functions."""
    # Chain operations: (2 + 3) * 4
    result1 = main.add(2, 3)
    result2 = main.multiply(result1, 4)
    assert result2 == 20.0
    
    # More complex: (10 - 2) / 2^2
    result1 = main.subtract(10, 2)
    result2 = main.power(2, 2)
    result3 = main.divide(result1, result2)
    assert result3 == 2.0
    
    # With string inputs
    result1 = main.add("10", "5")
    result2 = main.subtract(result1, "3")
    assert result2 == 12.0
