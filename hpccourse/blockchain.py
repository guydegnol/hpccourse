import hashlib
import time
import random
import pandas as pd

from .block import Block


# Display the BlockChain code on the side
# hpccourse.BlockChain??

import hashlib
import time
import random

random.seed(42)


class BlockChain:
    def __init__(self, reward_probability=0.1, miners_flops={"Aegon": 1.0}):
        # constructor method
        self.chain = []
        self.current_data = []
        self.nodes = set()
        self.lottery_range = int(1.0 / reward_probability)
        self.miners_flops = miners_flops
        self.construct_genesis()
        self.portfolios = {}
        self.start = time.time()
        self.transactions = []

    def construct_genesis(self):
        # constructs the initial block
        self.construct_block(proof_no=0, prev_hash=0)

    def construct_block(self, proof_no, prev_hash):
        # constructs a new block and adds it to the chain
        block = Block(index=len(self.chain), proof_no=proof_no, prev_hash=prev_hash, data=self.current_data)
        self.current_data = []

        self.chain.append(block)
        return block

    @staticmethod
    def check_validity(block, prev_block):
        # checks whether the blockchain is valid
        if prev_block.index + 1 != block.index:
            return False

        elif prev_block.calculate_hash != block.prev_hash:
            return False

        elif not BlockChain.verifying_proof(block.proof_no, prev_block.proof_no):
            return False

        elif block.timestamp <= prev_block.timestamp:
            return False

        return True

    def new_data(self, sender, recipient, quantity):
        # adds a new transaction to the data of the transactions
        self.current_data.append({"sender": sender, "recipient": recipient, "quantity": quantity})
        if sender not in self.portfolios:
            self.portfolios[sender] = 0
        if recipient not in self.portfolios:
            self.portfolios[recipient] = 0
        self.portfolios[sender] = -quantity
        self.portfolios[recipient] = quantity
        # print(f"{sender}-={quantity}, {recipient}+={quantity},  exec={time.time()-self.start}")

        self.transactions.append([sender, recipient, quantity, time.time() - self.start])
        self.start = time.time()

        return True

    def get_transactions(self):
        return pd.DataFrame(self.transactions, columns=["sender", "recipient", "quantity", "etime"])

    @staticmethod
    def proof_of_work(last_proof):
        """this simple algorithm identifies a number f' such that hash(ff') contain 4 leading zeroes
        f is the previous f'
        f' is the new proof
        """
        proof_no = 0
        while BlockChain.verifying_proof(proof_no, last_proof) is False:
            proof_no += 1

        return proof_no

    @staticmethod
    def verifying_proof(last_proof, proof):
        # verifying the proof: does hash(last_proof, proof) contain 4 leading zeroes?

        guess = f"{last_proof}{proof}".encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    @property
    def latest_block(self):
        return self.chain[-1]

    def update_miners_flops(self, miners_flops):
        self.miners_flops = miners_flops

    def construct_consolidated_block(self, sender, recipient, quantity, miner=None, reward_probability=None):
        self.start = time.time()
        self.new_data(sender=sender, recipient=recipient, quantity=quantity)
        last_block = self.latest_block
        last_proof_no = last_block.proof_no
        self.construct_block(last_proof_no, last_block.calculate_hash)

        lottery_range = int(1.0 / reward_probability) if reward_probability is not None else self.lottery_range
        if random.randint(0, lottery_range) != 1:
            return

        recipient = (
            miner
            if miner is not None
            else random.choices(list(self.miners_flops.keys()), weights=self.miners_flops.values(), k=1)[0]
        )
        self.block_mining(miner=miner, reward_probability=reward_probability)
        last_block = self.latest_block
        last_proof_no = last_block.proof_no
        self.construct_block(last_proof_no, last_block.calculate_hash)

    def block_mining(self, miner=None, reward_probability=None):

        self.new_data(sender="MINER_REWARD_!!!!!", recipient=miner, quantity=1)

        last_block = self.latest_block

        last_proof_no = last_block.proof_no
        proof_no = self.proof_of_work(last_proof_no)

        last_hash = last_block.calculate_hash

        block = self.construct_block(proof_no, last_hash)

        return vars(block)

    def create_node(self, address):
        self.nodes.add(address)
        return True

    @staticmethod
    def obtain_block_object(block_data):
        # obtains block object from the block data

        return Block(
            block_data["index"],
            block_data["proof_no"],
            block_data["prev_hash"],
            block_data["data"],
            timestamp=block_data["timestamp"],
        )
