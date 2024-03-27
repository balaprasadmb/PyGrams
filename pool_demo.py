'''
Created on 04-Apr-2023

@author: bprasad
'''
from multiprocessing import Pool

def func(a, b):
    return str(a)+str(b)

if __name__ == "__main__":
    pool_obj = Pool(2)
    print(dir(pool_obj))
    res = pool_obj.starmap(func, zip([1, 2], [3, 4]))
    print(dir(res))
    print(type(res))
    print(res)


