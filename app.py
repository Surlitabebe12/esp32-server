from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para permitir conexiones desde el ESP32

# Ruta para verificar que el servidor está activo
@app.route('/')
def home():
    return "Servidor funcionando correctamente"

# Ruta para recibir datos del ESP32
@app.route('/data', methods=['POST'])
def data():
    try:
        # Obtener datos en formato JSON
        json_data = request.get_json()
        
        if not json_data:
            return jsonify({"status": "error", "message": "No se enviaron datos"}), 400
        
        # Imprimir datos en consola
        print(f"Datos recibidos: {json_data}")
        
        # Responder al ESP32
        return jsonify({"status": "ok", "message": "Datos recibidos correctamente"}), 200
    
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"status": "error", "message": "Error en el servidor"}), 500

# Configuración para correr el servidor
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

