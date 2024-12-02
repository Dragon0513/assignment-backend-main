import sys
import os
import time
from sdk import GanacheSDK
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.append(os.path.abspath("ganache-be"))

def generate_wallet_with_prefix(prefix, max_retries=1000):
    ganache_sdk = GanacheSDK()
    
    # Function to generate a single wallet
    def generate_wallet():
        return ganache_sdk.generate_wallet()

    # Try a batch of wallets with threading for parallel generation
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(generate_wallet) for _ in range(max_retries)]
        
        # Collect completed wallet generation tasks
        for future in as_completed(futures):
            wallet = future.result()
            if wallet[0].startswith(prefix):
                return wallet
    return None  # Return None if no wallet is found with the prefix after max_retries

def main():
    start_time = time.time()
    wallet = generate_wallet_with_prefix('0x1234')
    if wallet:
        print(f"Wallet found: {wallet}")
    else:
        print("No wallet found with the specified prefix.")
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")

if __name__ == '__main__':
    if GanacheSDK().verify_certificate():
        main()
    else:
        print(
            'Error -1: Ganache is not yet installed or configured properly. Please run "python setup_ganache.py" to install it.')
