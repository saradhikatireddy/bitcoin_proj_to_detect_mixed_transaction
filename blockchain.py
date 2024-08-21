import requests

class Blockchain:
    def __init__(self, api_url="https://api.blockcypher.com/v1/btc/main/"):
        self.api_url = api_url

    def get_address_transactions(self, address):
        response = requests.get(f"{self.api_url}addrs/{address}/full")
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching transactions for {address}: {response.status_code}")
            return None
