# MAC Address lookup script

This script allows you to check the vendor of a specific mac address.

You can use this script from linux bash, WSL or Windows CMD/Powershell.<br>
You must have "python3 installed" with "requests" library and internet connection.<br>
`$ pip install requests`<br>

For help you can run:<br>
`$ python3 maclookup.py help`<br>

It is possible to concatenate several mac addresses in any form:<br>
`$ maclookup2.py 3C6AA771CCCB 00:50:56:C0:00:02 E4-B9-7A-08-C9-EF 001C.7F00.00010`<br>

This script uses public API from macvendors.com.<br>
For detail you can read the documentation at https://macvendors.com/api
