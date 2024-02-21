import json
from time import sleep
import requests

class auth():

    def __init__(self, access_token="", print_error=True, producao=False):
        self.access_token = access_token
        self.base_url = "https://api.asaas.com" if producao else "https://sandbox.asaas.com/api"
        self.print_error = print_error

    def request(self, method="GET", url="", headers=None, params=None, data=None, json=None):

        req_params = params if params != None or params != {} else None
        req_headers = headers if headers != None or headers != {} else None
        req_data = data if data != None or data != {} else None
        req_json = json if json != None or json != {} else None

        while True:

            match method:
                case "GET":
                    response = requests.get(url=url, params=req_params, headers=req_headers, data=req_data, json=req_json)
                case "PUT":
                    response = requests.put(url=url, params=req_params, headers=req_headers, data=req_data, json=req_json)
                case "POST":
                    response = requests.post(url=url, params=req_params, headers=req_headers, data=req_data, json=req_json)
                case "DELETE":
                    response = requests.delete(url=url, params=req_params, headers=req_headers, data=req_data, json=req_json)
                case "HEAD":
                    response = requests.head(url=url, params=req_params, headers=req_headers, data=req_data, json=req_json)
                case "OPTIONS":
                    response = requests.options(url=url, params=req_params, headers=req_headers, data=req_data, json=req_json)

            if response.status_code == 200 or response.status_code == 201:
                return response
            elif response.status_code != 429:
                if self.print_error:
                    try:
                        error_msg = f"""Mensagem: {response.json()['message'] if 'message' in response.json().keys() else response.json()}"""
                    except:
                        error_msg = f"""Mensagem:"""

                    try:
                        json_msg = f"""JSON: {response.json()}"""
                    except:
                        json_msg = f"""JSON: {response.text}"""

                    print(f"""Erro no retorno da API do Asaas
{error_msg}
Código: {response.status_code}
URL: {url}
Metodo: {method}
Parametros: {req_params}
Headers: {req_headers}
Data: {req_data}
{json_msg}""".replace(self.access_token, "********"))
                break
            else:
                sleep(5)

class cliente(auth):

    def buscar_clientes(self, name=None, email=None, cpfCnpj=None, groupName=None, externalReference=None, offset=None, limit=None):
        """
        Descrição da função
        """
        #Descrição da função

        asct = True #Acesso Só Com Token

        if asct and (self.access_token == "" or self.access_token == None or type(self.access_token) != str):
            print("Token inválido")
            return {}

        url = self.base_url+f"/v3/customers"

        headers = {
            "accept": "application/json",
            #'Content-Type': 'application/json',
            "access_token": self.access_token
        }

        params = {}

        if name:
            params['name'] = name
        if email:
            params['email'] = email
        if cpfCnpj:
            params['cpfCnpj'] = cpfCnpj
        if groupName:
            params['groupName'] = groupName
        if externalReference:
            params['externalReference'] = externalReference
        if offset:
            params['offset'] = offset
        if limit:
            params['limit'] = limit

        response = self.request("GET", url=url, headers=headers, params=params)

        if response:

            return response.json()
        
        else:
            return {}

    def criar_cliente(self, dados_cliente):
        """
        Descrição da função
        """
        #Descrição da função

        asct = True #Acesso Só Com Token

        if asct and (self.access_token == "" or self.access_token == None or type(self.access_token) != str):
            print("Token inválido")
            return {}

        url = self.base_url+f"/v3/customers"

        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'access_token': self.access_token
        }

        response = self.request("POST", url=url, headers=headers, json=dados_cliente)

        if response:

            return response.json()
        
        else:
            return {}
        
class assinatura(auth):

    def criar_assinatura(self, assinatura):
        """
        Descrição da função
        """
        #Descrição da função

        asct = True #Acesso Só Com Token

        if asct and (self.access_token == "" or self.access_token == None or type(self.access_token) != str):
            print("Token inválido")
            return {}

        url = self.base_url+f"/v3/subscriptions"

        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'access_token': self.access_token
        }

        response = self.request("POST", url=url, headers=headers, json=assinatura)

        if response:

            return response.json()
        
        else:
            return {}
        
    def atualizar_assinatura(self, id_assinatura, assinatura):
        """
        Descrição da função
        """
        #Descrição da função

        asct = True #Acesso Só Com Token

        if asct and (self.access_token == "" or self.access_token == None or type(self.access_token) != str):
            print("Token inválido")
            return {}

        url = self.base_url+f"/v3/subscriptions/{id_assinatura}"

        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'access_token': self.access_token
        }

        response = self.request("PUT", url=url, headers=headers, json=assinatura)

        if response:

            return response.json()
        
        else:
            return {}
        
    def ver_assinatura(self, id_assinatura):
        """
        Descrição da função
        """
        #Descrição da função

        asct = True #Acesso Só Com Token

        if asct and (self.access_token == "" or self.access_token == None or type(self.access_token) != str):
            print("Token inválido")
            return {}

        url = self.base_url+f"/v3/subscriptions/{id_assinatura}"

        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'access_token': self.access_token
        }

        response = self.request("GET", url=url, headers=headers)

        if response:

            return response.json()
        
        else:
            return {}
        
    def cobrancas_assinatura(self, id_assinatura):
        """
        Descrição da função
        """
        #Descrição da função

        asct = True #Acesso Só Com Token

        if asct and (self.access_token == "" or self.access_token == None or type(self.access_token) != str):
            print("Token inválido")
            return {}

        url = self.base_url+f"/v3/subscriptions/{id_assinatura}/payments"

        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'access_token': self.access_token
        }

        response = self.request("GET", url=url, headers=headers)

        if response:

            return response.json()
        
        else:
            return {}
