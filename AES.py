from Cryptodome.Cipher import AES

def AES_enc_algo(data,key):
    #convert to byte format
    if type(data) != bytes:
        data = data.encode()

    #generating a 16 bit key and converting it to byte format
    key_in = str(key)
    key_in = key_in[:16]
    key = key_in.encode()

    #AES encoding 
    cipher = AES.new(key, AES.MODE_EAX)
    cipher_text = cipher.encrypt(data)
    #iv = cipher.iv


    return cipher_text #iv

def AES_dec_algo(cipher_text,key):
    #generating a 16 bit key and converting it to byte format
    key_in = str(key)
    key_in = key_in[:16]
    key = key_in.encode()
    
    #decoding the message
    decrypt_cipher = AES.new(key, AES.MODE_EAX) #iv=iv
    data = decrypt_cipher.decrypt(cipher_text).decode()

    return data