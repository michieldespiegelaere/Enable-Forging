<h1>This is a tool to re enable forging after your lisk node stopped forging.</h1>

<h2>Setup</h2>

<p>to be able to run the python script you need to run pyhton -m pip install requests first so the script can execute the api calls and cUrl requests.</p>

<p>In EnableForging.py you need to configere the following variables:</p>
<ul>
  <li>ipAddress = '' # Your nodes ipaddress</li>
  <li>port = '' # The port you're using for your api</li>
  <li>publicKey = '' # The public key of the forging delegate</li>
  <li>password = '' # The password you used for encrypting your passphrase</li>
</ul>

<p>After installing the requests module you can start the script with python EnableForging.py or python3 EnableForging.py.</p>

<p>when you checked if everything runs well you can make a cronjob to have optimal us of the script.</p>

<p>P.S. script still in development for easier usage.</p>
