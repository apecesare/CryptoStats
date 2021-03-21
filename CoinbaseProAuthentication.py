import json, hmac, hashlib, time, requests, base64
from requests.auth import AuthBase
import time



api_key = 'e68a06e6ff3155d59e4879cd1732fe11'
api_secret = '9RjjnBtNzIvnDQdbUKxMc/IT4vtnsXMX3RujmFgNU27FyyRzxK7kCm+mEj41uRdBeIAfO2GIa0v07kXxvaUXrg=='
api_pass = 'kqj9gu4irvg'



# Create custom authentication for Exchange
class CoinbaseExchangeAuth(AuthBase):
    def __init__(self, api_key, secret_key, passphrase):
        self.api_key = api_key
        self.secret_key = secret_key
        self.passphrase = passphrase
    def __call__(self, request):
        timestamp = str(time.time())
        message = timestamp + request.method + request.path_url +     (request.body or '')
        hmac_key = base64.b64decode(self.secret_key)
        signature = hmac.new(hmac_key, message.encode('utf-8'), hashlib.sha256)
        signature_b64 = base64.b64encode(signature.digest())
        request.headers.update({
            'CB-ACCESS-SIGN': signature_b64,
            'CB-ACCESS-TIMESTAMP': timestamp,
            'CB-ACCESS-KEY': self.api_key,
            'CB-ACCESS-PASSPHRASE': self.passphrase,
            'Content-Type': 'application/json'
        })
        return request

api_url = 'https://api.pro.coinbase.com/'
auth = CoinbaseExchangeAuth(api_key, api_secret, api_pass)

def getTime():
  localtime = time.asctime( time.localtime(time.time()) )
  return localtime

def algo():
  r = requests.get(api_url + 'products/ALGO-EUR/ticker', auth=auth)
  data = json.loads(r .text)
  message = "Algorand: "
  message += json.dumps(data['price'])
  message += " Euro\n"
  return message

def btc():
  r = requests.get(api_url + 'products/BTC-EUR/ticker', auth=auth)
  data = json.loads(r .text)
  message = "Bitcoin: "
  message += json.dumps(data['price'])
  message += " Euro\n"
  return message

def eth():
  r = requests.get(api_url + 'products/ETH-EUR/ticker', auth=auth)
  data = json.loads(r .text)
  message = "Etherum: "
  message += json.dumps(data['price'])
  message += " Euro\n"
  return message

def ltc():
  r = requests.get(api_url + 'products/LTC-EUR/ticker', auth=auth)
  data = json.loads(r .text)
  message = "Litecoin: "
  message += json.dumps(data['price'])
  message += " Euro\n"
  return message

def xlm():
  r = requests.get(api_url + 'products/XLM-EUR/ticker', auth=auth)
  data = json.loads(r .text)
  message = "Stellar: "
  message += json.dumps(data['price'])
  message += " Euro\n"
  return message

def eos():
  r = requests.get(api_url + 'products/EOS-EUR/ticker', auth=auth)
  data = json.loads(r .text)
  message = "Eos: "
  message += json.dumps(data['price'])
  message += " Euro\n"
  return message

def bch():
  r = requests.get(api_url + 'products/BCH-EUR/ticker', auth=auth)
  data = json.loads(r .text)
  message = "Bitcoin Cash: "
  message += json.dumps(data['price'])
  message += " Euro\n"
  return message

def riassunto():
  mex = "["+getTime()+"]" + "\n\n"
  mex += algo() + btc() + eth() + ltc() + xlm() + eos() + bch()
  return mex

def algoStats():
  r = requests.get(api_url + 'products/ALGO-EUR/ticker', auth=auth)
  data = json.loads(r .text)
  message = "Algorand:\n"
  message += " - PREZZO EURO -> " + json.dumps(data['price']+"Euro")
  r = requests.get(api_url + 'products/ALGO-USD/ticker', auth=auth)
  data = json.loads(r .text)
  message += "\n - PREZZO USD -> " + json.dumps(data['price']+"USD ")
  return message

def bicoinStats():
  r = requests.get(api_url + 'products/BTC-EUR/ticker', auth=auth)
  data = json.loads(r .text)
  message = "Bitcoin:\n"
  message += " - PREZZO EURO -> " + json.dumps(data['price']+"Euro")
  r = requests.get(api_url + 'products/BTC-USD/ticker', auth=auth)
  data = json.loads(r .text)
  message += "\n - PREZZO USD -> " + json.dumps(data['price']+"USD ")
  return message

def etherumStats():
  r = requests.get(api_url + 'products/ETH-EUR/ticker', auth=auth)
  data = json.loads(r .text)
  message = "Etherum:\n"
  message += " - PREZZO EURO -> " + json.dumps(data['price']+"Euro")
  r = requests.get(api_url + 'products/ETH-USD/ticker', auth=auth)
  data = json.loads(r .text)
  message += "\n - PREZZO USD -> " + json.dumps(data['price']+"USD ")
  return message
