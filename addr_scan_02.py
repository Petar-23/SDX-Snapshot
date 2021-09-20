from tqdm import tqdm
import numpy as np
from web3 import Web3, HTTPProvider

# Iter over all blocks to capture all tx

w3 = Web3(HTTPProvider('https://rpc.swapdex.net'))
addr_lst = []
header = ['from', 'to']
block_range = 10000000
for block in tqdm(range(500000, block_range)):
    # print(block)
    try:
        # Get transaction by block
        # Loop through transaction index
        tx_flag = True
        i = 0
        while tx_flag == True:
            try:
                block_attr = w3.eth.get_transaction_by_block('{}'.format(hex(block)),i)
                addr_lst.append(block_attr['from'])
                addr_lst.append(block_attr['to'])
                i = i+1
            except:
                tx_flag = False
    except:
        print('Something went wrong')

addr_lst = list(dict.fromkeys(addr_lst))

# Save list of wallets as csv file
np.savetxt("wallet_addr_2.csv", addr_lst, delimiter=", ", fmt='% s')
print(addr_lst)