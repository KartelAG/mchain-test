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
w3.middleware_stack.inject(geth_poa_middleware, layer=0)
accountsByIP[bootNodeIP] = w3.eth.accounts

#print(w3.eth.getBlock('154285'))
latestBlockNumber = w3.eth.blockNumber

#print(latestBlockNumber)
#typeof(latestBlockNumber)

#block = w3.eth.getBlock(154355)
num = latestBlockNumber - 1500
while num < latestBlockNumber:
  num = num + 1
  print(w3.eth.getBlock(num).miner)

