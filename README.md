# SkyNFT-Royalty-Spend
    # This file is used for spend your SkyNFT royalty smart coins.
    # Just need your input two values, FIRST_ADDRESS and ROYALTY_PERCENTAGE
    # This file is open source by SkyNFT
    # Need full node support !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    
    # cd chia-blockchain
    # . activate
    # cd Your SkyNFT-Royalty_Spend dir
    # python3 skynft_drivers.py
    
    # SkyNFT will spend these coin every hours, but you can also spend your royalty coins by this code.
    # SkyNFT 250 is forbidden.
    # I do not want open other github account, so just this code into here.
    # Thanks
    
    ROYALTY_PUZZLE_HASH:068955e61c855fb324bf1ca0774db564fddd2047d3e2cf32f1a3e1d378eb1ecb

    ROYALTY_ADDRESS:xch1q6y4tesus40mxf9lrjs8wnd4vn7a6gz8603v7vh350sax78trm9sas7kkw

    You can open this url https://skynft.org/addressview.php?address=xch1q6y4tesus40mxf9lrjs8wnd4vn7a6gz8603v7vh350sax78trm9sas7kkw to check the unspend coins

    unspend coin_record:{'coin': {'amount': 45000000000,
              'parent_coin_info': '0x0fded225e8e878793c9911aee4499f1991c45b7aed230cf37829d3e0f9321083',
              'puzzle_hash': '0x068955e61c855fb324bf1ca0774db564fddd2047d3e2cf32f1a3e1d378eb1ecb'},
     'coinbase': False,
     'confirmed_block_index': 2194072,
     'spent_block_index': 0,
     'timestamp': 1656647545}
    {
        "aggregated_signature": "0xc00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "coin_solutions": [
            {
                "coin": {
                    "amount": 45000000000,
                    "parent_coin_info": "0x0fded225e8e878793c9911aee4499f1991c45b7aed230cf37829d3e0f9321083",
                    "puzzle_hash": "0x068955e61c855fb324bf1ca0774db564fddd2047d3e2cf32f1a3e1d378eb1ecb"
                },
                "puzzle_reveal": "0xff02ffff01ff02ffff01ff02ffff03ffff09ff17ffff018200fa80ffff01ff04ff06ffff04ff0bffff04ff2fff80808080ffff01ff02ffff03ffff15ff17ffff018200fa80ffff01ff02ffff03ffff15ffff018205ddff1780ffff01ff04ffff04ff04ffff04ff2fff808080ffff04ffff04ff06ffff04ff05ffff04ffff13ffff12ffff11ff17ffff018200fa80ff2f80ff1780ff80808080ffff04ffff04ff06ffff04ff0bffff04ffff13ffff12ffff018200faff2f80ff1780ff80808080ff80808080ffff01ff088080ff0180ffff01ff088080ff018080ff0180ffff04ffff01ff4933ff018080ffff04ffff01a04c4ad02bb7ee88529df4fa8beae1793804a365abb6aed2b18cfa6d2c3bd30bc2ffff04ffff01a032660603960cc5b5b16fe4a5e7300ca858c4e625e08ac1d3dd476fb811dd670bffff04ffff018201f4ff0180808080",
                "solution": "0xff850a7a35820080"
            }
        ]
    }
    {
        "status": "SUCCESS",
        "success": true
    }
    