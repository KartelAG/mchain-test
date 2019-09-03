#!/usr/bin/python3.6

from web3 import Web3
from web3.middleware import geth_poa_middleware
import random
import time

random.seed

accountsByIP = {
}
bootNodeIP = '192.168.201.12'

def getAccountsFromNodeIP(ip):
  connectionString = "http://"+ip+":20000"
  tempw3 = Web3(Web3.HTTPProvider(connectionString))
  return tempw3.eth.accounts

def getBalance(ip, addr):
  connectionString = "http://"+ip+":20000"
  tempw3 = Web3(Web3.HTTPProvider(connectionString))
  return tempw3.eth.getBalance(addr)

def sendTransaction(ip, addrFrom, addrTo, amount):
  connectionString = "http://"+ip+":20000"
  tempw3 = Web3(Web3.HTTPProvider(connectionString))
  tempw3.middleware_stack.inject(geth_poa_middleware, layer=0)
  tempw3.personal.unlockAccount(addrFrom, '')
  return tempw3.eth.sendTransaction({'from': addrFrom, 'to': addrTo, 'value': amount})

w3 = Web3(Web3.HTTPProvider("http://"+bootNodeIP+":20000"))
accountsByIP[bootNodeIP] = w3.eth.accounts

for i in w3.admin.peers:
  ip = (i['network']['remoteAddress']).split(':')[0]
  accountsByIP[ip] = 'empty'

for i in accountsByIP:
  accountsByIP[i] = getAccountsFromNodeIP(i)

num = 0
while num < 1000:
  num = num + 1
  txHash = ''
  print("Generating transaction N", num)
  selectedIPFrom = random.choice(list(accountsByIP.keys()))
  selectedAccountFrom = random.choice(accountsByIP[selectedIPFrom])

  selectedIPTo = random.choice(list(accountsByIP.keys()))
  selectedAccountTo = random.choice(accountsByIP[selectedIPTo])

  value = random.randint(10,100)

  balanceFrom = getBalance(selectedIPFrom, selectedAccountFrom)
  balanceTo = getBalance(selectedIPTo, selectedAccountTo)
  
  if (balanceFrom >= value):
    try:
      txHash = sendTransaction(selectedIPFrom, selectedAccountFrom, selectedAccountTo, value)
      print(','.join((str(time.asctime()), str(value), selectedIPFrom, selectedAccountFrom, str(balanceFrom), selectedAccountTo, str(balanceTo), txHash.hex())))
    except:
      print(time.asctime(), "##############some error has been occured!################")
  #time.sleep(random.randint(0,2))
  time.sleep(0.200)
