import requests
import time
import Config
import logging

ipAddress = Config.ipAddress       # Gets your nodes ipaddress from the config file
port = Config.port                 # Gets the port you're using for your api from the config file
publicKey = Config.publicKey       # Gets the public key of the forging delegate from the config file
password = Config.password         # Gets the password you used for encrypting your passphrase from the config file
logname = Config.logname           # Gets the name for your log file from the config file


def checkForging(ip, port, publicKey, password):

    url = 'http://' + ip + ':' + port + '/api/node/status/forging'
    json_data = requests.get(url).json()
    getData = json_data['data']
    headers = {'cache-control': 'no-cache', 'content-type': 'application/json'}
    data = '{"publicKey": "'+ publicKey +'","password": "' + password + '","forging": true}'

# gets the forging status out of the api call
    for i in getData:
        forging = i['forging']
        print(forging)

# checks if forging is running
# if forging isn't running it should re enable it
    if forging != True:
        print('Your node is not forging :\'(')
        logging.warning('Forging is disabled, trying to enable it again')
        print('Enabling forging now...')
        response = requests.put(url, data=data, headers=headers)
        time.sleep(2)
        responseData = response.json()
        print(responseData)
        getForgingResponseData = responseData['data']
        for i in getForgingResponseData:
            forging = i['forging']
        if forging != True:
            logging.warning('Forging is still disabled, trying to enable it for the last time')
            print('Something went wrong :\'(')
            #still needs to be tested
            time.sleep(10)
            response = requests.put(url, data=data, headers=headers)
            respondeData = response.json()
            getForgingResponseData = respondeData['data']
            for i in getForgingResponseData:
                forging = i['forging']
            if forging != True:
                logging.error('Can\'t ennable forging')
                print('Forging is disabled')
            else:
                logging.info('Your node started forging again')
                print('Forging is enabled again')
        else:
            logging.info('Your node is forging')
            print('Forging is enabled again :D')
    else:

        print('Your node is forging :)')
if __name__ == '__main__':
    logging.basicConfig(filename=logname, level=logging.INFO ,filemode='a+', format='%(asctime)s %(levelname)s %(message)s')
    checkForging(ipAddress, port, publicKey, password)