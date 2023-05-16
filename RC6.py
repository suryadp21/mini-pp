from RC6Encryption import RC6Encryption
from hashlib import sha256
from random import randbytes
import re

#       Revest Cipher 6

def rc6_enc_algo(data,key):
    #Initialize iv to 0 to make sure no element is sliced if iv is not initialised
    iv = 0
    
    while True:
        try: 
            if(len(data) != 16):
                if(type(data)==str):
                    #Converting the data to 16 byte form
                    data_1 = str(data)
                    while True:
                        if (len(data) < 16):
                            data_1 = data_1.zfill(16)
                            break
                        elif (len(data) > 16):
                            data_1 = data_1[:16]
                            break
                    
                    data = data_1.encode()
                else:
                    #length of the padded data
                    iv = 16 - len(data)
                    
                    #Padding the data with a random byte string
                    padding = randbytes(iv)
                    data = padding+data    

            #key
            key_in = str(key)
            key = key_in.encode()
            
            #rc6 encryption
            rc6 = RC6Encryption(sha256(key).digest())
            cipher = rc6.blocks_to_data(rc6.encrypt(data))

            return cipher,iv
        
        except (ValueError,TypeError):
            continue

def rc6_dec_algo(cipher,iv,key):
    
    #key conversion
    key_in = str(key)
    key = key_in.encode()

    #rc6 decryption
    rc6 = RC6Encryption(sha256(key).digest())
    decipher = rc6.blocks_to_data(rc6.decrypt(cipher))

    #Removing the padding from decipher
    decipher = decipher[iv:]

    return decipher    

def rc6_decode_mod(decipher):
    
    #Decoding and removing the padding using regex
    data = decipher.decode()
    regexPattern = "^0+(?!$)"
    data = re.sub(regexPattern, "", data)

    return data


