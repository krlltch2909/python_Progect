from cryptography.fernet import Fernet

# ключ для примера, при выгрузке обязателен к смене
cipher_key = b'LNPwLWnYdKxiy1Pb-462LLcAzMF6z37htxB9MNI-asI='
#
# cipher_key = Fernet.generate_key()


def cript_password(password):
    cipher = Fernet(cipher_key)
    encrypted_text = cipher.encrypt(password)
    #print(encrypted_text)
    return encrypted_text


# Дешифруем
def decrip_password(ciphertext):
    cipher = Fernet(cipher_key)
    decrypted_text = cipher.decrypt(ciphertext)
   # print(decrypted_text)
    return decrypted_text

