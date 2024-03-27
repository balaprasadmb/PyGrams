'''
Created on Nov 30, 2022

@author: bborade
'''
from cryptography.fernet import Fernet

message = "Some Message"

#key = Fernet.generate_key()

#print(key)

fernet = Fernet("pa4aVonRQ4GyPWWB-jT2uHsylEyBsZsYcKUWthh_8Lk=")

print(dir(fernet))

'''
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
'__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
'__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
'_decrypt_data', '_encrypt_from_parts', '_encryption_key', '_get_unverified_token_data', '_signing_key',
'_verify_signature', 'decrypt', 'decrypt_at_time', 'encrypt', 'encrypt_at_time', 'extract_timestamp', 'generate_key']
'''

encMessage = fernet.encrypt(message.encode())

print("Original Message String: ", message)
print("Encrypted Message String: ", encMessage)

decMessage = fernet.decrypt("gAAAAABjh0oEa7ru_ENiHpEspfnAHAfcP-TchwVAxtgqx0HBFEnr0J2dUO1PfrTiQvme7Ngnb9gok2isPMv6O4kJLy5OKFU3EQ==").decode()

print("Decrypted Message String: ", decMessage)
