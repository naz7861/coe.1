from flask import Flask, request, jsonify

app = Flask(__name__)

def count_inversions(arr):
    # (The count_inversions function from above)
    # Add the function implementation here
    pass

@app.route('/inversion_count', methods=['POST'])
def inversion_count():
    data = request.get_json()
    array = data.get('array', [])
    if not isinstance(array, list):
        return jsonify({"error": "Invalid input format. 'array' should be a list."}), 400

    try:
        inversions = count_inversions(array)
        return jsonify({"inversion_count": inversions})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
