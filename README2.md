# Bitcoin Transaction Parser with BitcoinRPC

## Overview

This Python script, `bitcoin_transaction_parser_rpc.py`, fetches Bitcoin transaction details, including block hashes, using Bitcoin Core's RPC (Remote Procedure Call) and the `bitcoinrpc` library. The results are logged to a text file named `btc_output.txt` for easy reference.

## Prerequisites

- Bitcoin Core installed and configured with RPC.
- Python 3.
- `bitcoinrpc` library installed. You can install it using:
  ```bash
  `pip install python-bitcoinrpc`
  
1. **Edit the script:**

Open bitcoin_transaction_parser_rpc.py in a text editor.
Set your Bitcoin Core RPC credentials in rpc_user and rpc_password.
Adjust the rpc_port if your Bitcoin Core RPC is configured on a different port.
Ensure the transaction_hashes list contains the desired Bitcoin transaction hashes.

2. **Run the script:**
`python3 bitcoin_transaction_parser_rpc.py`


