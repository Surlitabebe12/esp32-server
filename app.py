from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Servidor funcionando correctamente"

@app.route('/data', methods=['POST'])
def data():
    # Recibir datos JSON
    json_data = request.get_json()
    
    # Verificar si se recibieron datos
    if json_data:
        # Mostrar datos en los logs
        print(f"Datos recibidos: {json_data}")
        
        # Responder con éxito
        return jsonify({
            "status": "ok",
            "message": "Datos recibidos correctamente"
        }), 200
    else:
        # Responder con error si no se recibieron datos
        print("Error: No se enviaron datos.")
        return jsonify({
            "status": "error",
            "message": "No se enviaron datos"
        }), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
