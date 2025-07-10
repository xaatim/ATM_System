from flask import Flask, request, jsonify

app = Flask(__name__)

nfc_data = {"content": None}

@app.route('/nfc', methods=['POST', 'GET','DELETE'])
def handle_nfc():
    if request.method == 'POST':
        data = request.json
        nfc_data["content"] = data
        return jsonify({"status": "OK", "received": data})
    
    elif request.method == 'GET':
        return jsonify({"content": nfc_data["content"]})
    elif request.method == 'DELETE':
        print("Exiting")
        nfc_data["content"] = None
        

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000,debug=False)