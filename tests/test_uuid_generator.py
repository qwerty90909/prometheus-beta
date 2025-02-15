import re
import sys
import os

# Add src directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.uuid_generator import generate_uuid

def test_uuid_generation():
    """Test basic UUID generation."""
    uuid = generate_uuid()
    
    # UUID pattern based on RFC 4122 version 4
    uuid_pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$'
    assert re.match(uuid_pattern, uuid, re.IGNORECASE), f"Invalid UUID format: {uuid}"

def test_uuid_uniqueness():
    """Test that multiple UUID generations produce unique results."""
    uuids = set()
    for _ in range(100):
        uuid = generate_uuid()
        assert uuid not in uuids, "Duplicate UUID generated"
        uuids.add(uuid)

def test_uuid_version():
    """Verify UUID version and variant."""
    uuid = generate_uuid()
    
    # Check version (4th character of 3rd group should be 4)
    assert uuid.split('-')[2][0] == '4', "Incorrect UUID version"
    
    # Check variant (first character of 4th group should be 8, 9, a, or b)
    variant_char = uuid.split('-')[3][0]
    assert variant_char in ['8', '9', 'a', 'b'], "Incorrect UUID variant"

def test_uuid_length():
    """Verify UUID total length."""
    uuid = generate_uuid()
    assert len(uuid) == 36, f"Incorrect UUID length: {len(uuid)}"