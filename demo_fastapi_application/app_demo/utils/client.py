import httpx

# URL base del servidor local
base_url = "http://localhost:8000"

def create_user(username, password, service):
    data = {"email": username, "password": password}  # Datos del nuevo usuario
    response = httpx.post(service, json=data)
    if response.status_code == 201:
        print("Usuario creado exitosamente.")
    else:
        print("Error al crear el usuario:", response.status_code)

def login(username, password, service):
    data = {"username": username, "password": password}  # Datos de inicio de sesión
    response = httpx.post(service, json=data)
    if response.status_code == 200:
        token = response.json().get("token")
        print("Inicio de sesión exitoso.")
        print("Token de acceso:", token)
        return token
    else:
        print("Error al iniciar sesión:", response.status_code)
