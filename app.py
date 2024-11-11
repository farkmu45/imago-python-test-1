from flask import Flask, request, jsonify
from typing import List, Dict
from collections import defaultdict

app = Flask(__name__)

def transform_array(data: List[Dict]) -> Dict:
    """
    Transform a flat array of dictionaries into a three-level nested structure.
    
    Args:
        data: List of dictionaries containing id, name, category, and sub_category
        
    Returns:
        Dict: Three-level nested dictionary organized by category and sub_category
    """
    # Initialize nested defaultdict structure
    result = defaultdict(lambda: defaultdict(list))
    
    # Process each item in the input array
    for item in data:
        # Extract relevant fields
        category = item.get('category')
        sub_category = item.get('sub_category')
        
        # Create simplified item dictionary with only id and name
        simplified_item = {
            'id': item.get('id'),
            'name': item.get('name')
        }
        
        # Add item to appropriate nested location
        result[category][sub_category].append(simplified_item)
    
    # Convert defaultdict to regular dict for JSON serialization
    return {
        cat: dict(sub_cats)
        for cat, sub_cats in result.items()
    }

@app.route('/', methods=['POST'])
def transform():
    """
    API endpoint to transform the array structure.
    
    Expected JSON body format:
    [
        {"id": 1, "name": "Alice", "category": "A", "sub_category": "X"},
        ...
    ]
    """
    try:
        # Get JSON data from request
        data = request.get_json()
        
        # Validate input
        if not isinstance(data, list):
            return jsonify({'error': 'Input must be an array'}), 400
            
        for item in data:
            required_fields = {'id', 'name', 'category', 'sub_category'}
            if not all(field in item for field in required_fields):
                return jsonify({'error': f'Each item must contain fields: {required_fields}'}), 400
        
        # Transform the data
        result = transform_array(data)
        
        # Return transformed data
        return jsonify(result)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)