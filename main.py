from Crypto.Cipher import AES
import base64

# https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html

key = b'Sixteen byte key'
cipher = AES.new(key, AES.MODE_EAX)
data = b'some message'
nonce = cipher.nonce
ciphertext, tag = cipher.encrypt_and_digest(data)

print('cipher text = {0}'.format(ciphertext))
print('tag = {0} '.format(tag))

cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
plaintext = cipher.decrypt(ciphertext)

decodedString = plaintext.decode('utf-8')

try:
    cipher.verify(tag)
    print("The message is authentic:", plaintext)
    print('To string: ', decodedString)

except ValueError:
    print("Key incorrect or message corrupted")
