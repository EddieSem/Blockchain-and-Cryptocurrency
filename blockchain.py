# Initialising our blokchain list.
blockchain = []


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain """
    return blockchain[-1]


# Append to blockchain in the right order, default first.
def add_value(transaction_amount, last_transaction=[1]):
    """ Appends the last value of the current blockchain to the 
    front of the next blockchain 

    Arguments:
        :transaction-amount: The amount that should be added.
        :last_transaction: The last blockchain transaction (default [1]).
    """
    blockchain.append([last_transaction, transaction_amount])


def get_user_input():
    """ Returns the transaction amount the user inputs (float) """
    return float(input('Your transaction amount please: '))


tx_amount = get_user_input()
add_value(tx_amount)

tx_amount = get_user_input()
add_value(last_transaction=get_last_blockchain_value(),
          transaction_amount=tx_amount)

tx_amount = get_user_input()
add_value(tx_amount, get_last_blockchain_value())

print(blockchain)
