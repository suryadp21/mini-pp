from twofish import Twofish
from random import randbytes
import re

#       Twofish encryption

def Twofish_enc_algo(data,key):
    #Initialize iv to 0 to make sure no element is sliced if iv is not initialised
    iv = 0
    
    while True:
        try:
            #Converting the data to 16 byte form
            if(len(data) != 16):
                if(type(data)==str):
                    while True:
                        if (len(data) < 16):
                            data = data.zfill(16)
                            break
                        elif (len(data) > 16):
                            data = data[:16]
                            break
                    data = data.encode()
            
                else:
                    #length of the padded data
                    iv = 16 - len(data)
                    
                    #padding the data with a random byte string
                    padding = randbytes(iv)
                    data = padding+data

            #key conversion
            key_in = str(key)
            key = key_in.encode()
            
            #Genrating a Twofish Encryption key and Encrypt the data
            T = Twofish(key)
            cipher_text = T.encrypt(data)
            
            return cipher_text,iv
        
        except (ValueError,TypeError):
            continue

def Twofish_dec_algo(cipher_text,iv,key):
    
    #key conversion
    key_in = str(key)
    key = key_in.encode()
    
    #Genrating a Twofish Decryption key and Decrypt the data
    T = Twofish(key)
    decipher = T.decrypt(cipher_text)

    #Removing the padding from decipher
    decipher = decipher[iv:]

    return decipher
    
def Twofish_decode_mod(decipher):

    #Decoding and removing the padding using regex
    data = decipher.decode()
    regexPattern = "^0+(?!$)"
    data = re.sub(regexPattern, "", data)
    
    return data
