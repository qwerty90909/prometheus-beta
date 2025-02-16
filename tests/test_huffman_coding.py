import pytest
from src.huffman_coding import huffman_encode, huffman_decode, build_frequency_dict, build_huffman_tree, generate_huffman_codes

def test_build_frequency_dict():
    """Test frequency dictionary creation."""
    data = "hello world"
    freq_dict = build_frequency_dict(data)
    assert freq_dict == {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

def test_huffman_encode_basic():
    """Test basic Huffman encoding."""
    data = "hello"
    result = huffman_encode(data)
    
    # Verify result structure
    assert 'encoded' in result
    assert 'codes' in result
    assert 'original_data' in result
    assert result['original_data'] == data
    
    # Verify codes are unique
    assert len(set(result['codes'].values())) == len(result['codes'])

def test_huffman_encode_decode_round_trip():
    """Test full encode-decode round trip."""
    original_data = "hello world"
    encoded_result = huffman_encode(original_data)
    
    # Decode the data
    decoded_data = huffman_decode(encoded_result['encoded'], encoded_result['codes'])
    
    assert decoded_data == original_data

def test_huffman_encode_empty_string():
    """Test encoding an empty string."""
    result = huffman_encode("")
    assert result['encoded'] == ''
    assert result['codes'] == {}
    assert result['original_data'] == ''

def test_huffman_decode_empty_string():
    """Test decoding an empty string."""
    decoded = huffman_decode("", {})
    assert decoded == ''

def test_huffman_decode_invalid_encoded_data():
    """Test decoding with invalid encoded data."""
    codes = {'a': '0', 'b': '1'}
    with pytest.raises(ValueError, match="Invalid encoded data"):
        huffman_decode("10101010", codes)

def test_generate_huffman_codes():
    """Test Huffman code generation."""
    freq_dict = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}
    tree = build_huffman_tree(freq_dict)
    codes = generate_huffman_codes(tree)
    
    # Verify codes are created
    assert len(codes) == len(freq_dict)
    
    # Verify codes are unique
    assert len(set(codes.values())) == len(codes)

def test_complex_data_encoding():
    """Test encoding with more complex data."""
    data = "abracadabra"
    result = huffman_encode(data)
    decoded = huffman_decode(result['encoded'], result['codes'])
    
    assert decoded == data