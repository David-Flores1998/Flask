from flask import Flask, jsonify
import json

with open("API.json", "r") as json_api:
    datos_json = json.load(json_api)

app = Flask(__name__)

# Endpoint HTML
@app.route('/')
def inicio():
    print("Cambio")
    return datos_json["3D:AF:09:7F:00:01"]

# Endpoint JSON
@app.route('/json/<mac>')
def json_data(mac):
    print(datos_json[mac]["Name"])
    print(datos_json[mac]["Protocolos"])
    print(datos_json[mac]["VLANs"])
    return datos_json[mac]["Name"]

if __name__ == '__main__':
    app.run(debug=True)
@app.route('/')
def index():
    return """
    <html>
    <body>
        <h1>Hola mundo</h1>
        <a href="http://127.0.0.1:5000/api/saludo">Buscar Datos</a>
    </body>
    </html>

    """

# Datos incrustados (antes en API.json)
DISPOSITIVOS = {
    "101": {
        "ip": "192.168.1.10",
        "device_name": "Router Principal",
        "policy": {"type": "ALLOW_ALL"},
        "status": "Activo",
    },
    "102": {
        "ip": "192.168.1.20",
        "device_name": "Switch Piso 1",
        "policy": {"type": "BLOCK_IP", "blocked_ip": "192.168.1.20"},
        "status": "Activo",
    },
    "103": {
        "ip": "192.168.1.30",
        "device_name": "Firewall",
        "policy": {"type": "REQUIRED_IP", "required_ip": "192.168.1.30"},
        "status": "Activo",
    },
    "104": {
        "ip": "192.168.1.40",
        "device_name": "Servidor Web",
        "policy": {"type": "REQUIRED_IP", "required_ip": "192.168.1.50"},
        "status": "Activo",
    },
    "105": {
        "ip": "192.168.1.50",
        "device_name": "Access Point",
        "policy": {"type": "ALLOW_ALL"},
        "status": "Activo",
    },
        "106": {
        "ip": "192.168.1.60",
        "device_name": "Servidor de Base de Datos",
        "policy": {"type": "REQUIRED_IP", "required_ip": "192.168.1.60"},
        "status": "Activo",
    },
    "107": {
        "ip": "192.168.1.70",
        "device_name": "Cámara IP Entrada",
        "policy": {"type": "BLOCK_IP", "blocked_ip": "192.168.1.99"},
        "status": "Activo",
    },
    "108": {
        "ip": "192.168.1.80",
        "device_name": "Impresora Oficina",
        "policy": {"type": "ALLOW_ALL"},
        "status": "Inactivo",
    },
    "109": {
        "ip": "192.168.1.90",
        "device_name": "Servidor de Archivos",
        "policy": {"type": "REQUIRED_IP", "required_ip": "192.168.1.95"},
        "status": "Activo",
    },
    "110": {
        "ip": "192.168.1.100",
        "device_name": "Switch Piso 2",
        "policy": {"type": "BLOCK_IP", "blocked_ip": "192.168.1.100"},
        "status": "Activo",
    },
}

if __name__ == "__main__":
    app.run(debug=True)