'''
Created on Nov 30, 2022

@author: bborade
'''
import rsa

#key length should be atleast 16
publicKey, privateKey = rsa.newkeys(1024)

print(publicKey)

print(privateKey)

print(dir(rsa))

'''['DecryptionError', 'PrivateKey', 'PublicKey', 'VerificationError', '__all__', '__author__', '__builtins__',
'__cached__', '__date__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__',
'__version__', 'common', 'compute_hash', 'core', 'decrypt', 'encrypt', 'find_signature_hash', 'key', 'newkeys',
'pem', 'pkcs1', 'prime', 'randnum', 'sign', 'sign_hash', 'transform', 'verify']'''

message = "Some Message"

encMessage = rsa.encrypt(message.encode(),publicKey)#.hex()
 
print("Original Message String: ", message)
print("Encrypted Message String: ", encMessage)

decMessage = rsa.decrypt(encMessage, privateKey).decode()
 
print("Decrypted Message String: ", decMessage)
