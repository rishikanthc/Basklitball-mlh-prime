# import requests
# # r = requests.get('http://10.20.1.93:8090/key', data={'key':'value'})


# payload = {"source": "SPOTIFY", "type": "uri", "location": "spotify:track:6bRbeEgg8v8BQ0HuVuPE7v", "sourceAccount": "rishikanthc"}
# r = requests.post('http://10.20.1.93:8090/select', params=payload)
# print r.body

# import httplib, urllib
# params = urllib.urlencode({"ContentItem":{"source": "SPOTIFY", "type": "uri", "location": "spotify:track:6bRbeEgg8v8BQ0HuVuPE7v", "sourceAccount": "rishikanthc"}})
# headers = {"Content-Type": "application/json","Accept": "application/json"}
# conn = httplib.HTTPConnection("10.20.1.93:8090")
# conn.request("POST", "/select", params, headers)
# response = conn.getresponse()
# print response.status, response.reason
# data = response.read()
# conn.close()


import json
import requests
headers = 'Content-Type: application/json'
# head2 = 'Accept: application/json'
params = '{"ContentItem": {"source": "SPOTIFY", "type": "uri", "location": "spotify:track:6bRbeEgg8v8BQ0HuVuPE7v", "sourceAccount": "rishikanthc"}}'
parsed_json = json.loads(params)
# head = json.loads(headers)
print(parsed_json)


r = requests.post('http://10.20.1.93:8090/select',  headers, params )
print r
