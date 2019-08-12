blockchain = []

# Extract out last blockchain value and return it.
def get_last_blockchain_value():
    return blockchain[-1]


# Append to blockchain in the right order, default first. 
def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])

# Append to newly created initial block of the blockchain   
add_value(8)
# Return preivous block of the blockchain and append.
add_value(0.87, get_last_blockchain_value())
add_value(1010019874764.35365, get_last_blockchain_value())

print(blockchain)