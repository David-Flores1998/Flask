# Flask Project Reference

This project is a small Flask application that exposes device information from a JSON file and delivers a simple HTML landing page.

## Repository overview

- Application entry point: `App.py`
- Device data source: `Api.Json` / `API.json` (depending on the local file state)
- Supporting scripts: `C1.py`, `C2.py`, `C3.py`, `C4.py`, `Ejercicio.py`

## Current branch status

- Local branch: `feature/FlaskV01`
- Remote origin: not yet configured until the first push

## How the app starts

The application is initialized in `App.py` with:

```python
app = Flask(__name__)
```

It loads the JSON dataset with:

```python
with open("API.json", "r") as json_api:
    datos_json = json.load(json_api)
```

The server is started with:

```python
if __name__ == '__main__':
    app.run(debug=True)
```

## Route inventory

The current routes defined in `App.py` are:

| Route | Function | Method | Behavior |
| --- | --- | --- | --- |
| `/` | `inicio` | GET | Loads the record for the MAC address `3D:AF:09:7F:00:01` from the JSON and returns it directly as the response. |
| `/json/<mac>` | `json_data` | GET | Receives a MAC address from the URL, reads the related JSON object, prints its `Name`, `Protocolos`, `status`, and `VLANs` values to the terminal, and returns only the device name. |
| `/` | `index` | GET | Returns a simple HTML page with a link to `http://127.0.0.1:5000/api/saludo`. This page is intended as a landing page for testing, but the target route is not implemented in the file. |

## Route details

### 1) Root route

```python
@app.route('/')
def inicio():
    print("Cambio")
    return datos_json["3D:AF:09:7F:00:01"]
```

- URL: `/`
- Purpose: return the device information for the MAC address `3D:AF:09:7F:00:01`.
- Output: raw JSON object for that device.

### 2) JSON route by MAC

```python
@app.route('/json/<mac>')
def json_data(mac):
    print(datos_json[mac]["Name"])
    print(datos_json[mac]["Protocolos"])
    print(datos_json[mac]["status"])
    print(datos_json[mac]["VLANs"])
    return datos_json[mac]["Name"]
```

- URL: `/json/<mac>`
- Example: `/json/3D:AF:09:7F:00:01`
- Purpose: retrieve a device record using a MAC address as a dynamic parameter.
- Behavior:
  - logs the values of `Name`, `Protocolos`, `status`, and `VLANs`
  - returns only the device name as the HTTP response

### 3) HTML landing page

```python
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
```

- URL: `/`
- Purpose: display a simple HTML page with a link to a search endpoint.
- Important note: the page links to `/api/saludo`, but no route with that name is defined in `App.py`.

## Visual route map

```text
App
│
├── GET /
│   ├── inicio()
│   │   └── Returns the JSON entry for MAC 3D:AF:09:7F:00:01
│   │
│   └── index()
│       └── Returns a small HTML page with a link to /api/saludo
│
└── GET /json/<mac>
    └── json_data(mac)
        ├── Reads the device by MAC
        ├── Prints Name, Protocolos, status, VLANs
        └── Returns the device Name
```

## Notes for future development

- There are two route declarations for `/` in the same file; this should be cleaned up for clarity and to avoid duplicate route conflicts.
- The HTML page references `/api/saludo`, so a real route should be added if that feature is intended.
- The data model is nested under the loaded JSON object, which is the main source for the device records.
- The app currently uses `debug=True`, which is useful during local development but should be reviewed before deployment.

## Suggested next steps

1. Decide which `/` route should remain active and remove the duplicate definition.
2. Implement the missing `/api/saludo` route if needed.
3. Validate the JSON keys and the device MAC addresses.
4. Add error handling for unknown MAC addresses and invalid routes.
