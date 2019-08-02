blockchain = [[1]]

# Extract out last blockchain value and return it.
def get_last_blockchain_value():
    return blockchain[-1]

# Create the blockchain in one function. 
def add_value(transaction_amount):
    blockchain.append([get_last_blockchain_value(), transaction_amount])
    
add_value(8)
add_value(0.87)
add_value(1010019874764.35365)

print(blockchain)