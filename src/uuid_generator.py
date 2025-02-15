import time
import random
import os

def generate_uuid():
    """
    Generate a Universally Unique Identifier (UUID) without using external libraries.
    
    Returns:
        str: A unique 36-character UUID string in format 8-4-4-4-12
    """
    # Use current timestamp and system random seed for uniqueness
    random.seed(os.urandom(4))
    
    # Generate components of the UUID
    def hex_component(length):
        """Generate a random hexadecimal string of specified length."""
        return ''.join(random.choice('0123456789abcdef') for _ in range(length))
    
    # Time-low (8 hex characters)
    time_low = f'{int(time.time() * 1000) & 0xFFFFFFFF:08x}'
    
    # Time-mid (4 hex characters)
    time_mid = hex_component(4)
    
    # Time-high and version (first character is always 4 for version 4 UUID)
    time_high_version = f'4{hex_component(3)}'
    
    # Clock sequence (first character indicates variant 8 or 9, a, or b)
    clock_seq_high_reserved = f'8{hex_component(1)}'
    clock_seq_low = hex_component(2)
    
    # Node (12 hex characters)
    node = hex_component(12)
    
    # Combine into standard UUID format: 8-4-4-4-12
    return f'{time_low}-{time_mid}-{time_high_version}-{clock_seq_high_reserved}{clock_seq_low}-{node}'