import asyncio
from blspy import G2Element
import json

import time

from chia.rpc.full_node_rpc_client import FullNodeRpcClient
from chia.rpc.wallet_rpc_client import WalletRpcClient
from chia.types.blockchain_format.coin import Coin
from chia.types.blockchain_format.program import Program
from chia.types.blockchain_format.sized_bytes import bytes32
from chia.types.coin_spend import CoinSpend
from chia.types.spend_bundle import SpendBundle
from chia.util.bech32m import encode_puzzle_hash, decode_puzzle_hash
from chia.util.config import load_config
from chia.util.default_root import DEFAULT_ROOT_PATH
from chia.util.ints import uint16, uint64
from chia.wallet.transaction_record import TransactionRecord
from pathlib import Path
from chia.util.byte_types import hexstr_to_bytes
from sim import load_clsp_relative

config = load_config(DEFAULT_ROOT_PATH, "config.yaml")
self_hostname = config["self_hostname"] # localhost
full_node_rpc_port = config["full_node"]["rpc_port"] # 8555
wallet_rpc_port = config["wallet"]["rpc_port"] # 9256
prefix = "xch"


def print_json(dict):
    print(json.dumps(dict, sort_keys=True, indent=4))

async def getAllUnspentCoins(ROYALTY_PUZZLE_HASH, ROYALTY_PUZZLE):  
    try:
        node_client = await FullNodeRpcClient.create(self_hostname, uint16(full_node_rpc_port), DEFAULT_ROOT_PATH, config)
        all_royalty_coins = await node_client.get_coin_records_by_puzzle_hash(ROYALTY_PUZZLE_HASH,False,2180000)
        for coin_record in all_royalty_coins:
            coin_record = await node_client.get_coin_record_by_name(coin_record.coin.name())
            print(f"unspend coin_record:{coin_record}")        
            #Spent Coin
            coin_spend = CoinSpend(
                coin_record.coin,
                ROYALTY_PUZZLE,
                Program.to([coin_record.coin.amount])
            )
            # empty signature i.e., c00000.....
            signature = G2Element()
            # SpendBundle
            spend_bundle = SpendBundle(
                    # coin spends
                    [coin_spend],
                    # aggregated_signature
                    signature,
                )
            print_json(spend_bundle.to_json_dict())
            status = await node_client.push_tx(spend_bundle)
            print_json(status)            
    finally:
        node_client.close()
        await node_client.await_closed()

def MakeUserRoyaltyAddressBaseOnSkyNft(FIRST_ADDRESS,ROYALTY_PERCENTAGE): 
    SKYNFT_MOD = load_clsp_relative("clsp/skynft.clsp")
    SKYNFT_PUZZLE_HASH = "32660603960cc5b5b16fe4a5e7300ca858c4e625e08ac1d3dd476fb811dd670b"
    #print(f"decode_puzzle_hash(FIRST_ADDRESS):{decode_puzzle_hash(FIRST_ADDRESS)}")
    ROYALTY_PUZZLE = SKYNFT_MOD.curry(decode_puzzle_hash(FIRST_ADDRESS), hexstr_to_bytes(SKYNFT_PUZZLE_HASH), ROYALTY_PERCENTAGE)
    ROYALTY_PUZZLE_HASH = ROYALTY_PUZZLE.get_tree_hash()
    ROYALTY_ADDRESS = encode_puzzle_hash(ROYALTY_PUZZLE_HASH,prefix)
    #print(f"ROYALTY_PUZZLE:{ROYALTY_PUZZLE}")
    print(f"ROYALTY_PUZZLE_HASH:{ROYALTY_PUZZLE_HASH}\n")
    print(f"ROYALTY_ADDRESS:{ROYALTY_ADDRESS}\n")
    print(f"You can open this url https://skynft.org/addressview.php?address={ROYALTY_ADDRESS} to check the unspend coins\n")
    return ROYALTY_PUZZLE_HASH,ROYALTY_PUZZLE
    
if __name__ == "__main__":
    
    # This file is used for spend your SkyNFT royalty smart coins.
    # Just need your input two values, FIRST_ADDRESS and ROYALTY_PERCENTAGE
    # This file is open source by SkyNFT
    # Need full node support !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    
    # This is your first address (index=0, master_sk_to_wallet_sk_unhardened)
    # Your can check this address in 'My Wallet' menu in SkyNFT
    FIRST_ADDRESS = "xch1f39dq2aha6y99805l2974cte8qz2xedtk6hd9vvvlfkjcw7np0pq6fet9z"
    # Input your royalty percentage. 3% please input 300
    ROYALTY_PERCENTAGE = 500

    # Make the royalty puzzle hash
    ROYALTY_PUZZLE_HASH,ROYALTY_PUZZLE = MakeUserRoyaltyAddressBaseOnSkyNft(FIRST_ADDRESS,ROYALTY_PERCENTAGE)

    asyncio.run(getAllUnspentCoins(ROYALTY_PUZZLE_HASH,ROYALTY_PUZZLE))

