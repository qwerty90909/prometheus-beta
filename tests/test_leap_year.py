import pytest
from src.leap_year import is_leap_year

def test_standard_leap_years():
    """Test standard leap years divisible by 4"""
    assert is_leap_year(2020) == True
    assert is_leap_year(2024) == True
    assert is_leap_year(2000) == True

def test_non_leap_years():
    """Test years that are not leap years"""
    assert is_leap_year(2021) == False
    assert is_leap_year(2100) == False
    assert is_leap_year(1900) == False

def test_century_years():
    """Test century years with special leap year rules"""
    assert is_leap_year(2000) == True   # Divisible by 400
    assert is_leap_year(1900) == False  # Divisible by 100 but not 400
    assert is_leap_year(2100) == False  # Divisible by 100 but not 400

def test_error_handling():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError):
        is_leap_year("2020")
    
    with pytest.raises(TypeError):
        is_leap_year(2020.5)
    
    with pytest.raises(ValueError):
        is_leap_year(0)
    
    with pytest.raises(ValueError):
        is_leap_year(-2020)