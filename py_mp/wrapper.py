from time import sleep
import requests

class auth():

    def __init__(self, access_token="", print_error=True):
        self.access_token = access_token
        self.base_url = "https://api.mercadopago.com"
        self.print_error = print_error

    def request(self, method="GET", url="", headers=None, params=None, data=None, json=None):

        req_params = params if params != None else {}
        req_headers = headers if headers != None else {}
        req_data = data if data != None else {}
        req_json = json if json != None else {}

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
                    print(f"""Erro no retorno da API do Mercado Livre
Mensagem: {response.json()['message'] if 'message' in response.json().keys() else response.json()}
Código: {response.status_code}
URL: {url}
Metodo: {method}
Parametros: {req_params}
Headers: {req_headers}
Data: {req_data}
JSON: {response.json()}""")
                break
            else:
                sleep(5)

    def refresh_token(self, client_id, client_secret, refresh_token):
        """
        Descrição da função
        """
        #Descrição da função

        asct = True #Acesso Só Com Token

        if asct and (self.access_token == "" or self.access_token == None or type(self.access_token) != str):
            print("Token inválido")
            return None
        
        seller_id = self.access_token.split('-')[-1]

        url = self.base_url+f"/users/{seller_id}/items/search"

        params = {
            'access_token': self.access_token,
        }

        response = self.request("GET", url=url, params=params)

        if response:
            return None
        else:

            headers = {
                'accept': 'application/json',
                'content-type': 'application/x-www-form-urlencoded',
            }

            data = {
                'grant_type': 'refresh_token',
                'client_id': client_id,
                'client_secret': client_secret,
                'refresh_token': refresh_token,
            }

            #response = requests.post(f'{self.base_url}/oauth/token', headers=headers, data=data)

            response = self.request("POST", url=f'{self.base_url}/oauth/token', headers=headers, data=data)

            if response:
                return response
            else:
                return None

class cliente:

    class get(auth):

        def buscar(self, email=None):
            """
            Descrição da função
            """
            #Descrição da função

            asct = True #Acesso Só Com Token

            if asct and (self.access_token == "" or self.access_token == None or type(self.access_token) != str):
                print("Token inválido")
                return {}

            url = self.base_url+f"/v1/customers/search"

            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {self.access_token}'
            }

            params = {}

            if email:
                params['email'] = email

            response = self.request("GET", url=url, headers=headers, params=params)

            if response:

                return response.json()
            
            else:
                return {}

        def unico(self, id_cliente=None):
            """
            Descrição da função
            """
            #Descrição da função

            asct = True #Acesso Só Com Token

            if asct and (self.access_token == "" or self.access_token == None or type(self.access_token) != str):
                print("Token inválido")
                return {}

            url = self.base_url+f"/v1/customers/{id_cliente}"

            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {self.access_token}'
            }

            response = self.request("GET", url=url, headers=headers)

            if response:

                return response.json()
            
            else:
                return {}

    class create(auth):

        def criar(self, dados={}):
            """
            Descrição da função
            """
            #Descrição da função

            asct = True #Acesso Só Com Token

            if asct and (self.access_token == "" or self.access_token == None or type(self.access_token) != str):
                print("Token inválido")
                return {}

            url = self.base_url+f"/v1/customers"

            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {self.access_token}'
            }

            response = self.request("POST", url=url, headers=headers, json=dados)

            if response:

                return response.json()
            
            else:
                return {}
            
        def salvar_cartao(self, id_cliente, dados):
            """
            Descrição da função
            """
            #Descrição da função

            asct = True #Acesso Só Com Token

            if asct and (self.access_token == "" or self.access_token == None or type(self.access_token) != str):
                print("Token inválido")
                return {}

            url = self.base_url+f"/v1/customers/{id_cliente}/cards"

            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {self.access_token}'
            }

            response = self.request("POST", url=url, headers=headers, json=dados)

            if response:

                return response.json()
            
            else:
                return {}

class preferencias:

    class get(auth):

        def buscar(self):
            """
            Descrição da função
            """
            #Descrição da função

            asct = True #Acesso Só Com Token

            if asct and (self.access_token == "" or self.access_token == None or type(self.access_token) != str):
                print("Token inválido")
                return []

            url = self.base_url+f"/checkout/preferences/search"

            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {self.access_token}'
            }

            response = self.request("GET", url=url, headers=headers)

            if response:

                return response.json()
            
            else:
                return {}
            
        def unico(self, id_preferencia):
            """
            Descrição da função
            """
            #Descrição da função

            asct = True #Acesso Só Com Token

            if asct and (self.access_token == "" or self.access_token == None or type(self.access_token) != str):
                print("Token inválido")
                return []

            url = self.base_url+f"/checkout/preferences/{id_preferencia}"

            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {self.access_token}'
            }

            response = self.request("GET", url=url, headers=headers)

            if response:

                return response.json()
            
            else:
                return {}
            
    class create(auth):

        def criar(self, dados):
            """
            Descrição da função
            """
            #Descrição da função

            asct = True #Acesso Só Com Token

            if asct and (self.access_token == "" or self.access_token == None or type(self.access_token) != str):
                print("Token inválido")
                return {}

            url = self.base_url+f"/checkout/preferences"

            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {self.access_token}'
            }

            response = self.request("POST", url=url, headers=headers, json=dados)

            if response:

                return response.json()
            
            else:
                return {}
        
class assinatura():

    class get(auth):

        def buscar(self):
            """
            Descrição da função
            """
            #Descrição da função

            asct = True #Acesso Só Com Token

            if asct and (self.access_token == "" or self.access_token == None or type(self.access_token) != str):
                print("Token inválido")
                return {}

            url = self.base_url+f"/preapproval/search"

            params = {
                'access_token': self.access_token,
            }

            response = self.request("GET", url=url, params=params)

            if response:

                return response.json()
            
            else:
                return {}
            
    class create(auth):

        def criar(self, dados={}):
            """
            Descrição da função
            """
            #Descrição da função

            asct = True #Acesso Só Com Token

            if asct and (self.access_token == "" or self.access_token == None or type(self.access_token) != str):
                print("Token inválido")
                return {}

            url = self.base_url+f"/preapproval"

            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {self.access_token}'
            }

            response = self.request("POST", url=url, headers=headers, json=dados)

            if response:

                return response.json()
            
            else:
                return {}
            
class planos():

    class get(auth):

        def buscar(self, **kwargs):
            """
            Descrição da função
            """
            #Descrição da função

            asct = True #Acesso Só Com Token

            if asct and (self.access_token == "" or self.access_token == None or type(self.access_token) != str):
                print("Token inválido")
                return {}

            url = self.base_url+f"/preapproval_plan/search"

            params = {
                'access_token': self.access_token,
            }

            params.update(kwargs)

            response = self.request("GET", url=url, params=params)

            if response:

                return response.json()
            
            else:
                return {}
            
        def unico(self, id_plano):
            """
            Descrição da função
            """
            #Descrição da função

            asct = True #Acesso Só Com Token

            if asct and (self.access_token == "" or self.access_token == None or type(self.access_token) != str):
                print("Token inválido")
                return {}

            url = self.base_url+f"/preapproval_plan/{id_plano}"

            params = {
                'access_token': self.access_token,
                'id': id_plano
            }

            response = self.request("GET", url=url, params=params)

            if response:

                return response.json()
            
            else:
                return {}
        
    class create(auth):

        def criar(self, dados={}):
            """
            Descrição da função
            """
            #Descrição da função

            asct = True #Acesso Só Com Token

            if asct and (self.access_token == "" or self.access_token == None or type(self.access_token) != str):
                print("Token inválido")
                return {}

            url = self.base_url+f"/preapproval_plan"

            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {self.access_token}'
            }

            response = self.request("POST", url=url, headers=headers, json=dados)

            if response:

                return response.json()
            
            else:
                return {}

class geral(auth):

    def refresh_token(self, client_id, client_secret, refresh_token):
        return super().refresh_token(client_id, client_secret, refresh_token)