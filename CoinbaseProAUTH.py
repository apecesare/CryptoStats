import json, hmac, hashlib, time, requests, base64
from requests.auth import AuthBase
import time

api_url = 'https://api.pro.coinbase.com/'

def getTime():
  localtime = time.asctime( time.localtime(time.time()) )
  return localtime

def algo():
  r = requests.get(api_url + 'products/ALGO-EUR/ticker')
  data = json.loads(r .text)
  message = "Algorand: "
  message += json.dumps(data['price'])
  message += " Euro\n"
  return message

def btc():
  r = requests.get(api_url + 'products/BTC-EUR/ticker')
  data = json.loads(r .text)
  message = "Bitcoin: "
  message += json.dumps(data['price'])
  message += " Euro\n"
  return message

def eth():
  r = requests.get(api_url + 'products/ETH-EUR/ticker')
  data = json.loads(r .text)
  message = "Etherum: "
  message += json.dumps(data['price'])
  message += " Euro\n"
  return message

def ltc():
  r = requests.get(api_url + 'products/LTC-EUR/ticker')
  data = json.loads(r .text)
  message = "Litecoin: "
  message += json.dumps(data['price'])
  message += " Euro\n"
  return message

def xlm():
  r = requests.get(api_url + 'products/XLM-EUR/ticker')
  data = json.loads(r .text)
  message = "Stellar: "
  message += json.dumps(data['price'])
  message += " Euro\n"
  return message

def eos():
  r = requests.get(api_url + 'products/EOS-EUR/ticker')
  data = json.loads(r .text)
  message = "Eos: "
  message += json.dumps(data['price'])
  message += " Euro\n"
  return message

def bch():
  r = requests.get(api_url + 'products/BCH-EUR/ticker')
  data = json.loads(r .text)
  message = "Bitcoin Cash: "
  message += json.dumps(data['price'])
  message += " Euro\n"
  return message

def finalMEX():
  mex = "[" + getTime() + "]\n\n"
  mex += algo() + btc() + eth() + ltc() + xlm() + eos() + bch()
  return mex
