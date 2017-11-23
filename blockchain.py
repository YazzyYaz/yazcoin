class Blockchain(object):
    """Blockchain Class to Store the Blockchain"""

    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_block(self):
        """Creates new block and adds it to the chain"""
        pass

    def new_transaction(self, sender, recipient, amount):
        """
        Creates a new transaction to go into the next mined block.
        :param sender: <str> Address of sender
        :param recipient: <str> Address of the recipient
        :param amount: <str> Amount
        :return: <int>The index of the block that will hold this transaction
        """

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })

        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        """Hashes a block"""
        pass

    @property
    def last_block(self):
        """Returns the last block in the chain"""
        pass
