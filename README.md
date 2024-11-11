## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/farkmu45/imago-python-test-1.git
cd imago-python-test-1
```

2. Create a virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install required packages:
```bash
pip install flask
```

## Running the Application

1. Ensure you're in the project directory and your virtual environment is activated

2. Run the Flask application:
```bash
python app.py
```

The server will start on `http://localhost:5000`

## API Usage

### Transform Endpoint

**URL:** `/transform`
**Method:** `POST`
**Content-Type:** `application/json`

#### Request Body Format
```json
[
    {
        "id": 1,
        "name": "Alice",
        "category": "A",
        "sub_category": "X"
    },
    {
        "id": 2,
        "name": "Bob",
        "category": "B",
        "sub_category": "Y"
    }
]
```

#### Success Response Format
```json
{
    "A": {
        "X": [
            {
                "id": 1,
                "name": "Alice"
            }
        ]
    },
    "B": {
        "Y": [
            {
                "id": 2,
                "name": "Bob"
            }
        ]
    }
}
```

### Testing the API

Using curl:
```bash
curl -X POST http://localhost:5000/transform \
     -H "Content-Type: application/json" \
     -d '[
         {"id": 3, "name": "Charlie", "category": "A", "sub_category": "Z"},
         {"id": 1, "name": "Alice", "category": "A", "sub_category": "X"},
         {"id": 2, "name": "Bob", "category": "B", "sub_category": "Y"}
     ]'
```