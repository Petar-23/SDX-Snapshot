import multiprocessing as mp
import pandas as pd
from tqdm import tqdm
import numpy as np
from web3 import Web3, HTTPProvider


w3 = Web3(HTTPProvider('http://0.0.0.0:8501'))


def get_holder_in_block_range(list):
    addr_lst = []
    for block in tqdm(range(list[0], list[1])):
        # print(block)
        try:
            # Get transaction by block
            # Loop through transaction index
            tx_flag = True
            i = 0
            while tx_flag == True:
                try:
                    block_attr = w3.eth.get_transaction_by_block('{}'.format(hex(block)), i)
                    addr_lst.append(block_attr['from'])
                    addr_lst.append(block_attr['to'])
                    i = i + 1
                except:
                    tx_flag = False
        except:
            print('Something went wrong')

    # dropping duplicates
    df = pd.DataFrame(addr_lst)
    df = df.drop_duplicates()
    # addr_lst = list(dict.fromkeys(addr_lst))

    # Save list of wallets as csv file
    df.to_csv("wallet_addr_{}_to_{}.csv".format(list[0], list[1]))



def run_parallel():
    list = [[0, 100000], [100001, 200000], [200001, 300000], [300001, 400000], [400001, 500000], [500001, 600000]]
    pool = mp.Pool(mp.cpu_count())
    pool.map(get_holder_in_block_range, list)
    print("Number of processors: ", mp.cpu_count())

# Driver code
if __name__ == '__main__':
    run_parallel()

