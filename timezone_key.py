import time
import pytz
import random
from datetime import datetime
from pytz import all_timezones

def key_gen():
      timeZ_rand = pytz.timezone(random.choice(all_timezones)) 
      
      dt_rand = datetime.now(timeZ_rand)

      timestamp = time.mktime(dt_rand.timetuple()) + dt_rand.microsecond/1e6
      
      val = random.randrange(-1000000000,1000000000)

      timestamp+val
      
      random.seed(timestamp)
      # Get a random number
      rand_key = random.random()
    
      # Print the random number
      return rand_key

key = key_gen()  
print(key)

      
