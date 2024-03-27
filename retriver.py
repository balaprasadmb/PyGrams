'''
Created on Jun 10, 2019
@author: bborade
'''
import sys
import xml.etree.ElementTree as ET

def retrive_trans_ids(inpath):
    trans_ids=[]
    tree = ET.parse(inpath)
    root = tree.getroot()
    for test_message in root.iter("msg"):
        logs = test_message.text.split('\n')
        for log in logs:
            if "AURUSPAY TRANSACTION ID:" in log:
                trans_ids.append(str(log.split(":")[1]).strip())
    return trans_ids

if __name__ == '__main__':
    id_file = open("trans_ids.txt", "w")
    trans_ids = []
    for i in range(1, len(sys.argv)):
        trans_ids.extend(retrive_trans_ids(sys.argv[i]))
    id_file.write("\n".join(trans_ids))
    
