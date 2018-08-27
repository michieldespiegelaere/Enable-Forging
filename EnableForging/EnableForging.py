import requests
import time
import Config
ipAddress = Config.ipAddress  # Gets your nodes ipaddress from the config file
port = Config.port            # Gets the port you're using for your api from the config file
publicKey = Config.publicKey  # Gets the public key of the forging delegate from the config file
password = Config.password    # Gets the password you used for encrypting your passphrase from the config file

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
            #still needs to be tested
            time.sleep(20)
            response
            respondeData = response.json()
            getForgingResponseData = respondeData['data']
            for i in getForgingResponseData:
                forging = i['forging']
            if forging == True:
                print('Forging is enabled again')
            else:
                print('Forging is disabled. We will try to enable it later')
if __name__ == '__main__':
    checkForging(ipAddress, port, publicKey, password)