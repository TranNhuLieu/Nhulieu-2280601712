# sha-256.py

import hashlib

def calculate_sha256_hash(data):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(data.encode('utf-8')) # Chuyển đổi dữ liệu thành bytes và cập nhật vào đối tượng hash (Convert data to bytes and update the hash object)
    return sha256_hash.hexdigest() # Trả về biểu diễn hex chuỗi hash (Return the hex representation of the hash string)

data_to_hash = input("Nhập dữ liệu để hash bằng SHA-256: ") # Enter data to hash using SHA-256
hash_value = calculate_sha256_hash(data_to_hash)
print("Giá trị hash SHA-256:", hash_value) # SHA-256 hash value