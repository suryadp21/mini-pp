import random 
import time
import AES as A
import Twofish as B
import RC6 as C
from timezone_key import key_gen

data = 'TEST'

#Mapping the function placeholders to different values
def mapping_func():
    algos  = ['A','B','C']
    mapped_algos_check = []
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
    size = 2 #random.randint(2,5)
  
    for i in range(0,size):
        seq_num = random.randint(1, 12)
        seq_list.append(seq_num)
    
    return seq_list


#Initialize an empty key stack
keys = []

#Encoding functions replacing and calling 

def encReplace(mapped_dict,algo_sequence): 
    for seq in range(len(algo_sequence)):
        for key in mapped_dict:
            if(algo_sequence[seq] == key):
                if(mapped_dict[key] == 'A'):
                    print(1)
                    key = key_gen()
                    #data  = A.AES_enc_algo(data,key)
                elif(mapped_dict[key] == 'B'):
                    print(2)
                    key = key_gen()
                    #data = B.Twofish_enc_algo(data,key)
                elif(mapped_dict[key] == 'C'):
                    print(3)
                    key = key_gen()
                    #data = C.rc6_enc_algo(data,key)
                keys.append(key)
   
    
    algo_sequence.reverse()
    return data

#Decoding functions replacing and calling 

def decReplace(mapped_dict,algo_sequence):  
    for seq in range(len(algo_sequence)):
        for key in mapped_dict:
            if(algo_sequence[seq] == key):
                if(mapped_dict[key] == 'A'):
                    print(1)
                    key = keys.pop()
                    #data = A.AES_dec_algo(data,key)
                elif(mapped_dict[key] == 'B'):
                    print(2)
                    key = keys.pop()
                    #data = B.Twofish_dec_algo(data,key)
                elif(mapped_dict[key] == 'C'):
                    print(3)
                    key = keys.pop()
                    #data = C.rc6_dec_algo(data,key)

    return data        





#Function calls 

mapped_dict = mapping_func()
algo_sequence = sequence()


encData = encReplace(mapped_dict,algo_sequence)
message = decReplace(mapped_dict,algo_sequence)

