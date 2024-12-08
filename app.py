from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Servidor funcionando correctamente"

@app.route('/data', methods=['POST'])
def data():
    json_data = request.get_json()
    if json_data:
        print(f"Datos recibidos: {json_data}")
        return jsonify({"status": "ok", "message": "Datos recibidos correctamente"}), 200
    else:
        return jsonify({"status": "error", "message": "No se enviaron datos"}), 400

