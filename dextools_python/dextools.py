import requests


class DextoolsAPI:
    def __init__(self, api_key, version="v1", useragent="API-Wrapper/0.1"):
        self.url = f"https://api.dextools.io/{version}"
        self._api_key = api_key
        self._headers = {"X-API-Key": self._api_key, "accept": "application/json", "User-Agent": useragent}

    def get_pair(self, chain, address):
        endpoint = "/pair"
        response = requests.get(self.url + endpoint, params={"chain": chain, "address": address}, headers=self._headers)
        return response.json()
    
    def get_token(self, chain, address, page=None, pageSize=None):
        endpoint = "/token"
        response = requests.get(self.url + endpoint, params={"chain": chain, "address": address, "page": page, "pageSize": pageSize}, headers=self._headers)
        return response.json()
    
    def get_chain_list(self, page=None, pageSize=None):
        endpoint = "/chain/list"
        response = requests.get(self.url + endpoint, params={"page": page, "pageSize": pageSize}, headers=self._headers)
        return response.json()
    
    def get_exchange_list(self, chain, page=None, pageSize=None):
        endpoint = "/exchange/list"
        response = requests.get(self.url + endpoint, params={"chain": chain, "page": page, "pageSize": pageSize}, headers=self._headers)
        return response.json()
