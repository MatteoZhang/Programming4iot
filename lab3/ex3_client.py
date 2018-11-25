import requests
import json

if __name__ == '__main__':
    print "----start----"
    r = requests.get('http://localhost:8080/slots?N=12&reversion=False')
    s = r.json()
    print json.dumps(s, indent=2)
