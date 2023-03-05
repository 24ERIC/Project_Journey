# 7-block-chain.md

[👉Tutorial](https://hackernoon.com/learn-blockchains-by-building-one-117428612f46) [👉Source Code](https://github.com/dvf/blockchain?ref=hackernoon.com)


# Note
- What does a Block look like?
    - Each Block has an index, a timestamp (in Unix time), a list of transactions, a proof (more on that later), and the hash of the previous Block.
    - example block
        ```python
            block = {
            'index': 1,
            'timestamp': 1506057125.900785,
            'transactions': [
                {
                    'sender': "8527147fe1f5426f9dd545de4b27ee00",
                    'recipient': "a77f5cdfa2934df3954a5c7c7da5df1f",
                    'amount': 5,
                }
            ],
            'proof': 324984774000,
            'previous_hash': "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
            }
        ```
- Proof of Work
    - 
- Bitcoin, the Proof of Work algorithm is called Hashcash


# File Structure
- create blockchain (1-5)
    - Blockchain.py
        - class is responsible for managing the chain. It will store transactions and have some helper methods for adding new blocks to the chain. 
- Step 2: Our Blockchain as an API (6-8)
    - example request for a transaction
        ```python
            {
            "sender": "my address",
            "recipient": "someone else's address",
            "amount": 5
            }
        ```
    - The Mining Endpoint
        - Calculate the Proof of Work
        - Reward the miner (us) by adding a transaction granting us 1 coin
        - Forge the new Block by adding it to the chain
- Step 3: Interacting with our Blockchain ()
    - $ python blockchain.py
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
    - Using Postman to make a GET request,
        - [postman install link]()
    - use curl example
        ```python
            curl -X POST -H "Content-Type: application/json" -d '{"sender": "d4ee26eee15148ee92c6cd394edd974e", "recipient": "someone-other-address", "amount": 5 }' "http://localhost:5000/transactions/new"
        ```
        - res
            ```python
                127.0.0.1 - - [27/Feb/2023 15:07:37] "POST /transactions/new HTTP/1.1" 201 -
            ```
        - reseat server
            ```python
                {
                "chain": [
                    {
                    "index": 1,
                    "previous_hash": 1,
                    "proof": 100,
                    "timestamp": 1506280650.770839,
                    "transactions": []
                    },
                    {
                    "index": 2,
                    "previous_hash": "c099bc...bfb7",
                    "proof": 35293,
                    "timestamp": 1506280664.717925,
                    "transactions": [
                        {
                        "amount": 1,
                        "recipient": "8bbcb347e0634905b0cac7955bae152b",
                        "sender": "0"
                        }
                    ]
                    },
                    {
                    "index": 3,
                    "previous_hash": "eff91a...10f2",
                    "proof": 35089,
                    "timestamp": 1506280666.1086972,
                    "transactions": [
                        {
                        "amount": 1,
                        "recipient": "8bbcb347e0634905b0cac7955bae152b",
                        "sender": "0"
                        }
                    ]
                    }
                ],
                "length": 3
                }
            ```


- Step 4: Consensus ()
    - Implementing the Consensus Algorithm
    - valid_chain()
        - is responsible for checking if a chain is valid by looping through each block and verifying both the hash and the proof.
    - resolve_conflicts()
        - is a method which loops through all our neighbouring nodes, downloads their chains and verifies them using the above method. If a valid chain is found, whose length is greater than ours, we replace ours.