from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Servidor funcionando correctamente"

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    if not data:
        return jsonify({"status": "error", "message": "No se enviaron datos"}), 400
    print(f"Datos recibidos: {data}")
    return jsonify({"status": "ok", "message": "Datos recibidos correctamente"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
