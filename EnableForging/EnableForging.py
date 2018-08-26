import requests
import time
ipAddress = '' # Your nodes ipaddress
port = '' # The port you're using for your api 
publicKey = '' # The public key of the forging delegate
password = '' # The password you used for encrypting your passphrase

def checkForging(ip, port, publicKey, password):
    url = 'http://' + ip + ':' + port + '/api/node/status/forging'
    json_data = requests.get(url).json()
    getData = json_data['data']
    headers = {'cache-control': 'no-cache', 'content-type': 'application/json'}
    data = '{"publicKey": "'+ publicKey +'","password": "' + password + '","forging": true}'

# gets the forging status out of the api call
    for i in getData:
        forging = i['forging']

# checks if forging is running
    if forging == True:
        print('Your node is forging :)')

    else:
# if forging isn't running it should re enable it
        print('Your node is not forging :\'(')
        print('Enabling forging now...')
        response = requests.put(url, data=data, headers=headers)
        time.sleep(2)
        responseData = response.json()
        getForgingResponseData = responseData['data']
        for i in getForgingResponseData:
            forging = i['forging']
        if forging == True:
            print('Forging is enabled again :D')
        else:
            print('Something went wrong :\'(')

if __name__ == '__main__':
    checkForging(ipAddress, port, publicKey, password)