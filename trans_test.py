import binascii
import datetime
import json
import requests

trans_url = "https://uat42.auruspay.com/auruspay/api/auruspayServices/transactionService"

sale = {"4.40": "00", "4.41": "18", "4.42": "P2PE NOT SUPPORTED", "1.1": "100000015311", "1.2": "818002", "1.3": "10057015",
    "2.1": "080472439", "2.2": "000B4FECFACC", "2.3": "10.20.10.129", "3.1": "15", "3.2": "Mx915", "3.3": "Reg2",
    "3.4": "00", "3.5": "17.00", "3.6": "1.8", "3.7": "RFS00190", "3.8": "1", "3.23": "10.20.10.248:9701", "4.1": "1",
    "4.2": "190391", "4.3": "3", "4.4": "4111111111111111%1D1227%1D123", "4.5": "1.00", "4.6": "0.00", "4.7": "0.00",
    "4.8": "0.00", "4.9": "0.00", "4.10": "0.00", "4.11": "1.00", "4.13": "000001", "4.15": "1", "4.16": "", "4.17": "",
    "4.18": "", "4.19": "", "4.20": "840", "4.21": "840", "4.22": "0", "4.23": "", "4.24": "", "4.25": "0000", "4.26": "1",
    "4.27": "", "4.28": "", "4.29": "000000000000000000", "4.30": "", "4.31": "", "4.32": "1", "4.34": "", "4.39": "",
    "4.69": "", "4.70": "", "4.75": "", "4.79": "0", "4.136": "", "5.1": "", "5.2": "", "5.3": "", "5.4": "", "5.5": "",
    "5.6": "", "5.7": "", "5.8": "4.0.0.2", "5.9": "01", "6.1": "Bpd", "6.2": "Msh", "6.3": "Brd", "6.4": "PDRG, NM",
    "6.5": "", "6.6": "Pbn", "6.7": "MH", "6.8": "IN", "6.9": "431401", "6.10": "7276391903", "6.11": "bpd@test.com",
    "6.17": "Dns", "6.18": "Bpd", "6.19": "Brd", "6.20": "PDRG, NM", "6.21": "", "6.22": "Pbn", "6.23": "MH", "6.24": "IN",
    "6.25": "431401", "6.26": "9561906560", "6.27": "dns@test.com", "7.1": "0.00", "7.2": "0.00", "7.3": "0.00", 
    "7.4": "001", "7.5": "1234567%1F1%1F1%7EProduct+1%7E2%7E5%7E%7E%7E%7E%7E%7E%7E%7E001%7EElectronic%27s%7EProductShortDec1%7E%1D", 
    "3.19": "", "3.21": "1.1", "4.36": "", "4.46": "", "4.47": "", "4.52": "", "5.13": "", "8.1": ""}


sale["4.18"] = datetime.datetime.today().strftime('%m%d%Y')

sale["4.19"] = datetime.datetime.today().strftime('%H%M%S')

payload = {"encryptionFlag": "00",
           "txnDateTime": sale["4.18"] + sale["4.19"],
           "formFactorId": sale["1.3"],
           "payload": "STX" +  binascii.hexlify(json.dumps(sale).encode()).decode() + "ETX"}

trans_headers = {"Content-Type": "application/json"}

trans_resp = requests.post(trans_url, json=payload, headers=trans_headers)

print("\n{0}Transaction: Sale{0}\nHeaders: {1},\n{0}Request{0}\n{2}".format("*"*10, trans_headers, json.dumps(payload)))

trans_resp = trans_resp.json()
print("{0}Response{0}\n{1}".format("*"*10, json.dumps(trans_resp)))
trans_resp_text = json.loads(binascii.unhexlify(trans_resp["response"].lstrip('STX').rstrip('ETX')).decode())
print("{0}Decoded Response{0}\n{1}".format("*"*10, json.dumps(trans_resp_text)))
assert "72.2" in trans_resp_text, "Expected Response Code(72.2) In Response"
assert "72.6" in trans_resp_text, "Expected Response Text(72.6) In Response"
assert trans_resp_text["72.2"] == "000", "Expected Response Code(72.2) 000 But Found " + trans_resp_text["72.2"]
assert trans_resp_text["72.6"] == "APPROVAL", "Expected Response Text(72.6) APPROVAL But Found " + trans_resp_text["72.6"]
