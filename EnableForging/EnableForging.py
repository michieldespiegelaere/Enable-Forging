import requests
import time
url = 'http://localhost:7000/api/node/status/forging' # api link
json_data = requests.get(url).json()
getData = json_data['data']
forging =''
headers = {'cache-control': 'no-cache', 'content-type': 'application/json'}

# gets the forging status out of the api call
for i in getData:
	forging = i['forging']

# checks if forging is running
if forging == True:
	print('Your node is forging :)')

else:
    # if forging isn't running it should re enable it
    print('Your node is not forging :\'(')
    print('Enabling forging now')
    
    data = '{"publicKey": "","password": "","forging": true}'
    response = requests.put('http://localhost:7000/api/node/status/forging', data=data, headers=headers)
    time.sleep(5)
    responseData = response.json()
    getForgingResponseData = responseData['data']
    for i in getForgingResponseData:
        forging = i['forging']
    if forging == True:
        print('Forging is enabled again')
    else:
        print('Something went wrong')
