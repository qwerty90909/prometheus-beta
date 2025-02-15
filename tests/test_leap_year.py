import pytest
from src.leap_year import is_leap_year

def test_standard_leap_years():
    """Test typical leap years"""
    assert is_leap_year(2000) == True
    assert is_leap_year(2004) == True
    assert is_leap_year(2020) == True
    assert is_leap_year(2024) == True

def test_standard_non_leap_years():
    """Test typical non-leap years"""
    assert is_leap_year(2001) == False
    assert is_leap_year(2002) == False
    assert is_leap_year(2003) == False
    assert is_leap_year(2100) == False

def test_century_exceptions():
    """Test century years with special rules"""
    assert is_leap_year(1900) == False  # Divisible by 100, not by 400
    assert is_leap_year(2000) == True   # Divisible by 400
    assert is_leap_year(2100) == False  # Next century year

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