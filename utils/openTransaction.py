import json
import requests
import subprocess
def emulateNFC(transactionID):
    subprocess.call(["sudo", "./nfc-emulate-forum-tag4", transactionID])

def openTransaction():
    
    data = {'amount': float(raw_input("Transaction Amount: ")), 'businessId':'LfgUKTixCd'}
    url = 'https://nathantannar.me/api/dev/functions/openTransaction'
    headers = {
        "X-Parse-Application-ID": "5++ejBLY/kzVaVibHAIIQZvbawrEywUCNqpD+FVpHgU=",
        "X-Parse-Master-Key": "oR3Jp5YMyxSBu6r6nh9xuYQD5AcsdubQmvATY1OEtXo=",
        "Content-Type": "application/json"
    }
    response = requests.post(url,data=json.dumps(data), headers=headers, verify=False)
    json_data = json.loads(response.text)
    if 'result' in json_data:
        print json_data['result']
        if 'objectId' in json_data['result']:
            transactionId = json_data['result']['objectId']
            print "Openned a transaction with id: " + transactionId
            emulateNFC(transactionId)
            
    if 'error' in json_data:
        print json_data['error']


openTransaction()
