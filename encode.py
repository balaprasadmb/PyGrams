import os
import json
import binascii

with open(os.path.dirname(__file__) + '/data_files/req.json', 'r') as jf:
    req_data = json.load(jf)
    print(binascii.hexlify(json.dumps(req_data).encode()))
    jf.close()
