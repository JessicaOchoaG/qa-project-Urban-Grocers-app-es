from http.client import responses

import configuration
import requests
import data

def post_create_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

def post_new_client_kit(kit_body, auth_Token):
    current_headers = data.headers.copy()
    current_headers ["Authorization"] = "Bearer " + auth_Token
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=current_headers)






