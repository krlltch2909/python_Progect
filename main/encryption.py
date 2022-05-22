
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

data = b"Hello world"
key = b'6\xeeo\xd4\x92p\x18y\xc3\xbbE\xa5q\xe8I\xc5'
#key = get_random_bytes(16) # Генерируем ключ шифрования

# Шифрование
cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)
nonce = cipher.nonce
print(ciphertext)
print(key)
print(nonce)
print(tag)# Зашифрованный текст

# Дешифровка
cipher = AES.new(key, AES.MODE_EAX, nonce)
data = cipher.decrypt_and_verify(ciphertext, tag)
print(data)