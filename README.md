# Dogecoin Transaction Parser

## Overview

This Python script, `doge_transaction_parser.py`, fetches Dogecoin transaction details, including block hashes, using the Dogecoin CLI. The results are logged to a text file named `doge_output.txt` for easy reference.

## Prerequisites

- Dogecoin Core installed with the Dog°ecoin CLI (`dogecoin-cli`).
- Python 3.

## Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/GreatApe42069/dogecoin-transaction-parser
   cd dogecoin-transaction-parser

**2. Edit the script:**

-Open `doge_transaction_parser.py` in a text editor.
-Set the correct path to your Dogecoin CLI (`dogecoin-cli`) in the `dogecoin_cli` variable.
-Ensure the transaction_hashes list contains the desired Dogecoin transaction hashes.

**3. Run the script:**

- `python3 doge_transaction_parser.py`

**4. Check the output:**

- The script will create a file named `doge_output.txt`

- This file contains entries like:
  *Transaction Hash: [transaction_hash], Block Hash: [block_hash]*

## Command Example: 
- `python3 doge_transaction_parser.py`

## Additional Use Cases

**Multiple Transaction Hashes:**

-You can extend the transaction_hashes list with multiple transaction hashes for batch processing.

## Integration with Other Systems:

- Integrate this script into larger systems or workflows to automate transaction-related tasks.

**Notes**
*Ensure that you have the necessary permissions to run the Dogecoin CLI.
If a block hash is not found for a transaction, the entry will indicate that*

## Contributors: GreatApe42069 , 






