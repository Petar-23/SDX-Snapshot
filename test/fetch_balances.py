from web3 import Web3, HTTPProvider

w3 = Web3(HTTPProvider('https://rpc.swapdex.net'))

balance = w3.eth.get_balance('0x9771f561EabF867D3D1cd8FA0Fb1ED6E287210b6', hex(3500000))
balance = w3.fromWei(balance, 'ether')

print(balance)