import requests
from ipify import get_ip
from ipify.exceptions import IpifyException

try:
    ip = get_ip()
    r = requests.get('http://usercountry.com/v1.0/json/' + ip)
    result = r.json()
    print(result['currency']['code'])
    print(result)
except IpifyException:
    print("exception from ipigy" + IpifyException)
except:
    print("other exceptions")