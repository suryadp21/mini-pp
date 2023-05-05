from twofish import Twofish
import re

def Twofish_enc_algo(data,key):
    if type(data) == bytes:
        data = data.decode()
    
    data_1 = str(data)
    #16 bytes conversion of data
    if(len(data) != 16):
        while True:
            if (len(data) < 16):
                data_1 = data_1.zfill(16)
                break
            elif (len(data) > 16):
                data_1 = data_1[:16]
                break

    
    #convert to byte format
    if type(data_1) != bytes:
        data = data_1.encode()
    
    #key
    key_in = str(key)
    key = key_in.encode()
    
    T = Twofish(key)
    
    cipher_text = T.encrypt(data)
    return cipher_text
    

def Twofish_dec_algo(cipher_text,key):
    
    key_in = str(key)
    key = key_in.encode()
    
    T = Twofish(key)
    data = T.decrypt(cipher_text).decode()
    
    regexPattern = "^0+(?!$)"
    data = re.sub(regexPattern, "", data)
    
    return data