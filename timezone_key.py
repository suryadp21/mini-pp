import time
import pytz
import random
from datetime import datetime
from pytz import all_timezones

#Generating a randomized key

def key_gen():
      #choosing a random timezone 
      timeZ_rand = pytz.timezone(random.choice(all_timezones)) 
      
      #getting the present time of that timezone
      dt_rand = datetime.now(timeZ_rand)

      #converting the timezone into a float value
      timestamp = time.mktime(dt_rand.timetuple()) + dt_rand.microsecond/1e6
      
      #Adding a random value between -10 billion to 10 billion 
      val = random.randrange(-1000000000,1000000000)

      timestamp+val
      
      random.seed(timestamp)
      # Get a random number
      rand_key = random.random()
    
      # Print the random number
      return rand_key

      
