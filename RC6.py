from RC6Encryption import RC6Encryption
from hashlib import sha256
import re

def rc6_enc_algo(data,key):
    
    if(len(data) != 16):
        #converting the data to 16 byte form
        data_1 = str(data)
        while True:
            if (len(data) < 16):
                data_1 = data_1.zfill(16)
                break
            elif (len(data) > 16):
                data_1 = data_1[:16]
                break
        
        data = data_1.encode()
    
    #key
    key_in = str(key)
    key = key_in.encode()

    #data = b'abcdefghijklmnop'
    
    #encryption 
    rc6 = RC6Encryption(sha256(key).digest())
    cipher = rc6.blocks_to_data(rc6.encrypt(data))

    return cipher

def rc6_dec_algo(cipher,key):
    
    #key
    key_in = str(key)
    key = key_in.encode()

    rc6 = RC6Encryption(sha256(key).digest())
    decipher = rc6.blocks_to_data(rc6.decrypt(cipher))
    data = decipher.decode()
    
    #removing padding using regex
    regexPattern = "^0+(?!$)"
    data = re.sub(regexPattern, "", data)

    return data

