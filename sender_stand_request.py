import configuration
import requests

def get_new_user_token(json_data):
    url = configuration.URL_SERVICE + configuration.CREATE_USER_PATH
    response = requests.post(url, json=json_data)
    dict_new_user = response.json()
    return dict_new_user["authToken"]

def post_new_client_kit(auth_token, kit_body):
    url = configuration.URL_SERVICE + configuration.KITS_PATH
    headers = {
        "Authorization": f"Bearer {auth_token}",  # Reemplaza automaticamente el valor del token generado.
        "Content-Type": "application/json"
    }
    # Indicamos el cuerpo,
    body = kit_body
    # Enviando la petición
    response = requests.post(url, json=body, headers=headers)  # Envia una peticion, ademas guarda la respuesta en una variable
    return response