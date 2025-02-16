from collections import Counter, defaultdict
import heapq

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def build_frequency_dict(data):
    """Build a frequency dictionary for the input data."""
    return Counter(data)

def build_huffman_tree(freq_dict):
    """Construct Huffman tree from frequency dictionary."""
    # Create heap of nodes
    heap = [HuffmanNode(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(heap)
    
    # Build tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        # Create internal node with these two nodes as children
        internal_node = HuffmanNode(None, left.freq + right.freq)
        internal_node.left = left
        internal_node.right = right
        
        heapq.heappush(heap, internal_node)
    
    return heap[0] if heap else None

def generate_huffman_codes(root):
    """Generate Huffman codes from the Huffman tree."""
    if not root:
        return {}
    
    codes = {}
    
    def traverse(node, current_code):
        if not node:
            return
        
        # Leaf node
        if node.char is not None:
            codes[node.char] = current_code
            return
        
        # Recurse left (add 0)
        if node.left:
            traverse(node.left, current_code + "0")
        
        # Recurse right (add 1)
        if node.right:
            traverse(node.right, current_code + "1")
    
    traverse(root, "")
    return codes

def huffman_encode(data):
    """
    Encode input data using Huffman coding.
    
    Args:
        data (str or list): Input data to encode
    
    Returns:
        dict: A dictionary containing:
            - 'encoded': Encoded binary string
            - 'codes': Huffman codes dictionary
            - 'original_data': Original input data
    """
    if not data:
        return {
            'encoded': '',
            'codes': {},
            'original_data': data
        }
    
    # Build frequency dictionary
    freq_dict = build_frequency_dict(data)
    
    # Build Huffman tree
    huffman_tree = build_huffman_tree(freq_dict)
    
    # Generate Huffman codes
    codes = generate_huffman_codes(huffman_tree)
    
    # Encode the data
    encoded = ''.join(codes[char] for char in data)
    
    return {
        'encoded': encoded,
        'codes': codes,
        'original_data': data
    }

def huffman_decode(encoded_data, codes):
    """
    Decode Huffman encoded data.
    
    Args:
        encoded_data (str): Binary encoded string
        codes (dict): Huffman codes dictionary
    
    Returns:
        str: Decoded original data
    """
    if not encoded_data:
        return ''
    
    # Invert the codes dictionary
    reverse_codes = {code: char for char, code in codes.items()}
    
    decoded = []
    current_code = ''
    
    for bit in encoded_data:
        current_code += bit
        if current_code in reverse_codes:
            decoded.append(reverse_codes[current_code])
            current_code = ''
    
    # Check if we successfully decoded everything
    if current_code:
        raise ValueError("Invalid encoded data: Could not fully decode")
    
    return ''.join(decoded)