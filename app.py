from flask import Flask, request, jsonify

app = Flask(__name__)

# Hardcoded user details
USER_ID = "john_doe_17091999"
EMAIL = "john@xyz.com"
ROLL_NUMBER = "ABCD123"

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome! Please use the /bfhl endpoint for API operations."}), 200

@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1}), 200

@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        # Retrieve 'data' from request JSON
        req_json = request.get_json()
        if not req_json or 'data' not in req_json:
            raise ValueError("Invalid input: JSON with 'data' key required.")

        data = req_json.get("data", [])
        if not isinstance(data, list):
            raise ValueError("Invalid data format: 'data' should be a list.")

        # Separate numbers and alphabets
        numbers = []
        alphabets = []

        for item in data:
            # Check if item is a number string (could be more than one digit)
            if item.isdigit():
                numbers.append(item)
            # If item is a single letter (alphabet) then include in alphabets
            elif len(item) == 1 and item.isalpha():
                alphabets.append(item)
            else:
                # In case item is neither, you can ignore or handle accordingly.
                pass

        # Determine highest_alphabet: the alphabet that comes last in the A-Z series (case-insensitive)
        highest_alphabet = [max(alphabets, key=lambda x: x.upper())] if alphabets else []

        response = {
            "is_success": True,
            "user_id": USER_ID,
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": highest_alphabet
        }
        return jsonify(response), 200

    except Exception as e:
        return jsonify({"is_success": False, "message": str(e)}), 400

if __name__ == '__main__':
    # Run the Flask app on port 7000 with debug mode enabled.
    app.run(debug=True, port=5000)
