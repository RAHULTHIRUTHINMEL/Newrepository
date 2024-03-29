import requests

api_key = 'pk_2fb1b05357f5435ebc6d14fcdd83b69f'
class CryptoCurrency:
    base_url = "https://cloud.iexapis.com/stable/crypto"
    def __init__(self,symbol):
        self.symbol = symbol

    @property
    def complete_url(self):
        return f"{CryptoCurrency.base_url}/{self.symbol}/price?token={api_key}"
    
    @property
    def price(self):
        req = requests.get(self.complete_url).json()   #this method will convrt json to dic
        return float(req.get("price"))             
