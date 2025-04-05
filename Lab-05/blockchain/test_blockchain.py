from blockchain import Blockchain

# Khởi tạo blockchain
my_blockchain = Blockchain()

# Nhập số lượng giao dịch
num_transactions = int(input("Nhập số lượng giao dịch muốn thêm: "))

# Nhập từng giao dịch thủ công
for i in range(num_transactions):
    print(f"\nGiao dịch #{i+1}")
    sender = input("Người gửi: ")
    receiver = input("Người nhận: ")
    amount = float(input("Số tiền: "))
    my_blockchain.add_transaction(sender, receiver, amount)

# Tiến hành mining (tạo block mới)
previous_block = my_blockchain.get_previous_block()
previous_proof = previous_block.proof
new_proof = my_blockchain.proof_of_work(previous_proof)
previous_hash = previous_block.hash
my_blockchain.add_transaction('Genesis', 'Miner', 1) 
new_block = my_blockchain.create_block(new_proof, previous_hash)

# Hiển thị toàn bộ blockchain
print("\n--- Blockchain ---")
for block in my_blockchain.chain:
    print(f"\nBlock #{block.index}")
    print("Timestamp:", block.timestamp)
    print("Transactions:", block.transactions)
    print("Proof:", block.proof)
    print("Previous Hash:", block.previous_hash)
    print("Hash:", block.hash)
    print("------------------------------")

# Kiểm tra tính hợp lệ của blockchain
print("Is Blockchain Valid:", my_blockchain.is_chain_valid(my_blockchain.chain))
