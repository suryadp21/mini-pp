from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto import Random
from random import randbytes
import re

#       Advanced Encryption System 

def AES_enc_algo(data,key):
    
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
                    
                    #padding the data with a random byte string
                    padding = randbytes(iv)
                    data = padding+data 
        
            #generating a 16 bit key and converting it to byte format
            key_in = str(key)
            key_in = key_in[:16]
            key = key_in.encode()
         
            #Counter for encryption and IV generator
            random_generator = Random.new()
            IV = random_generator.read(8)
            ctr_e = Counter.new(64, prefix=IV)

            #Aes encoding in CTR mode
            cipher = AES.new(key, AES.MODE_CTR , counter=ctr_e)
            cipher_text = cipher.encrypt(data)
            
            return cipher_text,IV
        
        except(ValueError,TypeError):
            continue

def AES_dec_algo(cipher_text,IV,key):
    #generating a 16 bit key and converting it to byte format
    key_in = str(key)
    key_in = key_in[:16]
    key = key_in.encode()
    
    #Counter for decryption
    ctr_d = Counter.new(64, prefix=IV)
    
    #Aes decoding in CTR mode
    decrypt_cipher = AES.new(key, AES.MODE_CTR , counter=ctr_d) #iv=iv
    decipher = decrypt_cipher.decrypt(cipher_text)

    return decipher

def AES_decode_mod(decipher):
    
    #Decoding and removing the padding using regex
    data = decipher.decode()
    regexPattern = "^0+(?!$)"
    data = re.sub(regexPattern, "", data)

    return data
