#!/usr/bin/env python3
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import json

# Bitcoin Core RPC configuration
rpc_user = 'your_rpc_username'
rpc_password = 'your_rpc_password'
rpc_port = 8332  # Default Bitcoin RPC port

# List of transaction hashes
transaction_hashes = [
    "1c0ffee123456789abcdef0123456789abcdef0123456789abcdef0123456789"
]

# Function to get block hash for a transaction hash
def get_block_hash(tx_hash):
    try:
        rpc_connection = AuthServiceProxy(f'http://{rpc_user}:{rpc_password}@localhost:{rpc_port}')
        tx_info = rpc_connection.gettransaction(tx_hash)
        # Assuming you're looking for the block hash where the transaction was included
        block_hash = tx_info.get('blockhash', None)
        return block_hash
    except JSONRPCException as e:
        print(f"Error: {e}")
        return None

# Print block hashes to btc_output.txt
with open("btc_output.txt", "a") as file:
    for tx_hash in transaction_hashes:
        block_hash = get_block_hash(tx_hash)
        if block_hash:
            file.write(f"Transaction Hash: {tx_hash}, Block Hash: {block_hash}\n")
        else:
            file.write(f"Transaction Hash: {tx_hash}, Block Hash not found\n")

print("Script executed successfully.")
