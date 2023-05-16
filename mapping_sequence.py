import random 
import time
import AES as A
import Twofish as B
import RC6 as C
from timezone_key import key_gen

data = input("Enter 16 byte data\n") 

#Mapping the function placeholders to different values
def mapping_func():
    algos  = ['A','B','C']
    mapped_algos_check = []
    
    #Mapping dictionary
    mapped_algos = {}

    for key in range(1,13):
        while True:
            algo = random.choice(algos)
            if algo not in mapped_algos_check:
                mapped_algos.update({key:algo})
                mapped_algos_check.append(algo)
                break
            
            if (len(mapped_algos_check) == 3 ):
                mapped_algos_check.clear()

    return mapped_algos


#Generating a sequence list for calling the enc and dec finctions in an order
def sequence():
    
    # Providing system time as the seed value
    random.seed(time.time())
    seq_list = []
    
    #Number of encryptions
    size = 100  # Fixed or random.randint(2,5)
  
    for i in range(0,size):
        seq_num = random.randint(1, 12)
        seq_list.append(seq_num)
    
    return seq_list


#Initialize an empty key stack,cipherText stack and iv_padding stack for Aes
#iv_num_t and iv_num_r as stacks for iv_num of Twofish and Rc6 

keys,cipherTexts,iv_stack,iv_num_t,iv_num_r = ([] for i in range(5))
 
#Encoding functions replacing and calling 

def encReplace(mapped_dict,algo_sequence): 
    #Sequence check and matching the algo_sequence to the mapped placeholders
    for seq in range(len(algo_sequence)):
       
        key = algo_sequence[seq]
        
        if(mapped_dict[key] == 'A'):
            
            if(seq == 0):
                key = key_gen()
                cipher,iv  = A.AES_enc_algo(data,key)
            else:    
                key = key_gen()
                cipher,iv  = A.AES_enc_algo(cipher,key)
            iv_stack.append(iv)
        
        elif(mapped_dict[key] == 'B'):
            
            if(seq == 0):
                key = key_gen()
                cipher,iv_num  = B.Twofish_enc_algo(data,key)
            else:    
                key = key_gen()
                cipher,iv_num = B.Twofish_enc_algo(cipher,key)
            iv_num_t.append(iv_num)

        elif(mapped_dict[key] == 'C'):
            
            if(seq == 0):
                key = key_gen()
                cipher,iv_num  = C.rc6_enc_algo(data,key)
            else:    
                key = key_gen()
                cipher,iv_num  = C.rc6_enc_algo(cipher,key)
            iv_num_r.append(iv_num)
        
        cipherTexts.append(cipher)    
        keys.append(key)
    
    print("The keys list for encryption and decryption : ",keys,"\n")
    
    algo_sequence.reverse()
    return cipher,cipherTexts

#Decalre a list to show the decoded byte strings 
decoded_data = []

#Decoding functions replacing and calling 

def decReplace(mapped_dict,algo_sequence,cipherTexts):  
    iv = b'xxxxxxxx' #Random initialising value
    iv_num = 0       #Random initialising value
    
    #Sequence check and matching the algo_sequence to the mapped placeholders
    for seq in range(len(algo_sequence)):
        key = algo_sequence[seq]
        
        #Popping the cipher texts and keys in the decryption order
        cipher = cipherTexts.pop()
        dec_keys = keys.pop()

        #Call the functions according to the sequnce and the decide mod when the last sequence is reached
        if(mapped_dict[key] == 'A'):
            
            if(len(iv_stack) > 0):
                iv = iv_stack.pop()
            
            if(seq == len(algo_sequence)-1):
                decipher = A.AES_dec_algo(cipher,iv,dec_keys)
                data = A.AES_decode_mod(decipher)
                break
            else:    
                cipher = A.AES_dec_algo(cipher,iv,dec_keys)
            
            
        elif(mapped_dict[key] == 'B'):
            
            if(len(iv_num_t) > 0):
                iv_num = iv_num_t.pop()
            
            if(seq == len(algo_sequence)-1):
                decipher = B.Twofish_dec_algo(cipher,iv_num,dec_keys)
                data = B.Twofish_decode_mod(decipher)
                break
            else:    
                cipher = B.Twofish_dec_algo(cipher,iv_num,dec_keys)
            

        elif(mapped_dict[key] == 'C'):

            if(len(iv_num_r) > 0):
                iv_num = iv_num_r.pop()
            
            if(seq == len(algo_sequence)-1):
                decipher  = C.rc6_dec_algo(cipher,iv_num,dec_keys)
                data = C.rc6_decode_mod(decipher)
                break
            else:    
                cipher = C.rc6_dec_algo(cipher,iv_num,dec_keys)
        
        #To show all decoded messages in the form a list
        decoded_data.append(cipher)

    return data        





#Function calls 

mapped_dict = mapping_func()
algo_sequence = sequence()

print("\nMapped dictionary: ",mapped_dict,"\n")
print("Algorithm sequence: ",algo_sequence,"\n")

#Encoding function call with the cipher text list
encData,cip = encReplace(mapped_dict,algo_sequence)
print("Encrypted data list : ",cip,"\n")

#Decoding function call with decrypted text list
message = decReplace(mapped_dict,algo_sequence,cip)
print("Decrypted data list : ",decoded_data,"\n")

print("The encrypted data is : ",encData,"\n")
print("The decrypted message is :",message,"\n")

