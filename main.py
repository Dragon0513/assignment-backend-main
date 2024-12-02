import sys
import os
sys.path.append(os.path.abspath("ganache-be"))
from sdk import GanacheSDK
import time


def generate_wallet_with_prefix(prefix):
    # TODO: - Please optimize time performance of this function. Only modify code in this function.
    ganache_sdk = GanacheSDK()
    wallet = ganache_sdk.generate_wallet()
    while wallet[0].startswith(prefix) is False:
        wallet = ganache_sdk.generate_wallet()
    return wallet 


def main():
    start_time = time.time()
    generate_wallet_with_prefix('0x1234')
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")


if __name__=='__main__':
    if GanacheSDK().verify_certificate():
        main()
    else:
        print(
            'Error -1: Ganache is not yet installed or configured properly. Please run "python setup_ganache.py" to install it.')