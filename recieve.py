from flask import request, jsonify

def receive_sensor():
    data = request.get_json(silent=True)

    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    print(data)

    return jsonify({"status": "received"}), 200