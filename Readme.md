<h1>This is a tool to re enable forging after your lisk node stopped forging.</h1>

<h2>Download</h2>

<p>To download the script you can just clone the project or download the files with wget </p>
<p>clone https://github.com/michieldespiegelaere/EnableForging.git</p>
<p>wget https://raw.githubusercontent.com/michieldespiegelaere/EnableForging/master/EnableForging/EnableForging.py & wget https://raw.githubusercontent.com/michieldespiegelaere/EnableForging/master/EnableForging/Config.py</p>

<h2>Setup</h2>

<p>To be able to run the python script you need to run pyhton -m pip install requests first so the script can execute the api calls and cUrl requests.</p>
<p>For the logging part you need to run python -m pip install logging </p>

<p>In Config.py you need to configere the following variables:</p>
<ul>
  <li>ipAddress = '127.0.0.1'  # Your forging nodes ipaddress</li>
  <li>port = '7000'       # The port you're using for your api betanet :5000 testnet:7000 mainnet:8000</li>
  <li>publicKey = ''  # The public key of the forging delegate</li>
  <li>password = ''   # The password you used for encrypting your passphrase</li>
  <li>logname = 'EnableForging.log'    # The name for your log file</li>
</ul>
<p>If you don't want logging you need to empty the logname variable</p>
<p>After installing the requests module you can start the script with python EnableForging.py or python3 EnableForging.py.</p>

<p>when you checked if everything runs well you can make a cronjob to have optimal us of the script.</p>

<h2>Creation of the cronjob</h2>
<p>The best way to make full use of the script is to run the script every minute as a cronjob. The following commands will show you how to create a cronjob that executes the script every minute.</p>
<ol>
  <li>Go to cron.hourly with: cd /etc/cron.hourly</li>
  <li>To make a cronjob use: crontab -e</li>
  <li>You'll enter in a text editor where you have to fill in your cronjob. To run the cronjob every minute you have to use the following line: * * * * * /usr/bin/python /home/lisk/lisk-test/EnableForging/EnableForging/EnableForging.py > /home/lisk/lisk-test/cron_EnableForging.log 2>&1
</li>
  <li>When you have edited the file just ctrl+x to save the file.</li>
</ol>
<p>The following link helped me a lot. https://awc.com.my/uploadnew/5ffbd639c5e6eccea359cb1453a02bed_Setting%20Up%20Cron%20Job%20Using%20crontab.pdf</p>


<p>P.S. script still in development for easier usage.</p>
