#!/usr/bin/python3.6

from web3 import Web3

logFile = open("log-2019-08-10.txt", "r")
logFileReader = logFile.readlines()

bootNodeIP = '192.168.201.12'
def getTXStatus(ip, txHash):
  connectionString = "http://"+ip+":20000"
  tempw3 = Web3(Web3.HTTPProvider(connectionString))
  return tempw3.eth.getTransactionReceipt(txHash)

def getTXHash(line):
  dataArray = line.split(",")
  return dataArray[len(dataArray)-1].replace("\n","")

for txLine in logFileReader:
  if (not(txLine.startswith("Generating")) and not("##############" in txLine)):
    txHash = getTXHash(txLine)
    txStatus = getTXStatus(bootNodeIP, txHash)
    if not(txStatus):
      print("Transaction", txHash, "was not approved!")
    else:
      print("OK:", txStatus['transactionHash'].hex(), txStatus['blockNumber'])

logFile.close()
