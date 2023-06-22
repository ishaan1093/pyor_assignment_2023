from datetime import datetime
from web3 import Web3

def get_block_numbers_by_date(date):
    # Connect to the Ethereum node using a provider
    web3 = Web3(Web3.HTTPProvider('https://chainlist.org/chain/1'))

    # Convert the input date to a Unix timestamp
    timestamp = int(datetime.strptime(date, '%Y-%m-%d').timestamp())

    # Get the latest block number
    latest_block_number = web3.eth.block_number

    # Iterate backwards from the latest block number to find the first block of the given date
    first_block_number = None
    for block_number in range(latest_block_number, 0, -1):
        block = web3.eth.get_block(block_number)
        if block.timestamp < timestamp:
            first_block_number = block_number + 1  # Add 1 to get the first block of the date
            break

    # If the first block number is not found, it means there are no blocks on or before the given date
    if first_block_number is None:
        return None

    # Get the block number of the latest block on the given date
    last_block_number = latest_block_number if first_block_number == latest_block_number else first_block_number - 1

    return first_block_number, last_block_number
