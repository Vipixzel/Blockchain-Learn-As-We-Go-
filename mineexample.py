from hashlib import sha256
import time

MAX_NONCE = 100000000000
#maximum # of iteration of the nonce

#defining the hashing
def SHA256(text):
    return sha256(text.encode('utf-8')).hexdigest()
#mining

def mine(block_number,transactions,previous_hash,prefix_zeros):
    prefix_str = "0" * prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"Block complete!: {nonce}")
            return new_hash
        
    raise BaseException(f"Block not executed...{MAX_NONCE} failed")
if __name__ == "__main__":
    transaction = """
        ("sender": "0x0", "recipient": "0x1", "amount": "100")
    """
    difficulty = 6
    #changing number will increase time for mining

    start = time.time()
    print("Starting Block....")
    new_hash = mine(
        5,
        transaction,
        "",
        difficulty,
    )
    total_time = str((time.time()- start))
    print(f"End of Block: {total_time} seconds")
    print(new_hash)