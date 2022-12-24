import rsa

def generateKeys():
    (public_key, private_key) = rsa.newkeys(1024)

    with open('keys/public.pem', 'wb') as p:
        p.write(public_key.save_pkcs1("PEM"))

    with open ('keys/private.pem', 'wb') as p:
        p.write(private_key.save_pkcs1("PEM"))

def loadKeys():
    with open('keys/publicKey.pem', 'wb') as p:
        publicKey = rsa.PublicKey.load_pkcs1(p.read())
    with open('keys/privateKey.pem', 'wb') as p:
        privateKey = rsa.PrivateKey.load_pkcs1(p.read())
    return privateKey, publicKey

def encrypt(message, key):
    return rsa.encrypt(message.encode('ascii'),key)  

def decrypt(ciphertext, key):
    try:
        return rsa.decrypt(ciphertext, key).decode('ascii')
    except:
        return False

def sign(message, key):
    return rsa.sign(message.encode('ascii'), key, 'SHA-1')

def verify(message, signature, key):
    try:
        return rsa.verify(message.encode('ascii'), signature,key,) == 'SHA-1'
    except:
        return False

generateKeys()
publicKey, privateKey =loadKeys()
message = input('Write your message here:')
ciphertext = encrypt(message, publicKey)
signature = sign(message, privateKey)
text = decrypt(ciphertext, privateKey)

print(f'Cipher text: {ciphertext}')
print(f'Signature: {signature}')


if text:
    print(f'Message text: {text}')
else:
    print(f'Unable to decrypt the message.')

if verify(text, signature, publicKey):
    print("Successfully verified signature")
else:
    print('The message signature could not be verified')
