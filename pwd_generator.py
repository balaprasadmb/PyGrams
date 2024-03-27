'''
Created on Oct 19, 2022

@author: bborade
'''
import random
import string

def get_random_string(max_len):
    rnd_str = ''
    for _ in range(max_len):
        rnd_str += ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits))
    print(rnd_str)

get_random_string(10)
