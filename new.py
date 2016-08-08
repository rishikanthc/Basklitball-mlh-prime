import logging
import requests
import xmltodict
from cached_property import cached_property_with_ttl
from pprint import pprint
SERIAL_PORT = "/dev/tty.usbmodem1421"
BAUD_RATE = 9600

import serial
import tweepy, time, sys

# argfile = str(sys.argv[1])

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = '97JgwtwX0gub3vE30ZhP6aKZs'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = '5gRcGRNFxQmglehMmMKkealtpszXXmpmzb2YRnOtV0lg6t97lY'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '1944376015-WjKOE2E4Ir2pznuKcncANbii0da3cPcYpAnsxZA'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'lB6lrpXzS1ibabKAq8YEnkBYJhYdzLHGT3IGFJE10Pzsv'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# CONSUMER_KEY = '12UlA77qo0vR60BOlIHYpKp1Q '#keep the quotes, replace this with your consumer key
# CONSUMER_SECRET = 'bU3KGkxQ1Zr39z1L98NeLeinN2ty7adpOyHZQAuE10aP6GEJA5'#keep the quotes, replace this with your consumer secret key
# ACCESS_KEY = '762192596093562880-rYjyT4LLQyk2gUAAnmJLNot7MmFblvh'#keep the quotes, replace this with your access token
# ACCESS_SECRET = 'qclY02XypsrcFSPqgK8uBtRXNsTPxzMBxkkkTqqUrsM57'#keep the quotes, replace this with your access token secret
# auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
# auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
# api = tweepy.API(auth)




log = logging.getLogger(__name__)


# -*- coding: utf-8 -*-

PLAY = "PLAY"
PAUSE = "PAUSE"
STOP = "STOP"
PREV_TRACK = "PREV_TRACK"
NEXT_TRACK = "NEXT_TRACK"
THUMBS_UP = "THUMBS_UP"
THUMBS_DOWN = "THUMBS_DOWN"
BOOKMARK = "BOOKMARK"
POWER = "POWER"
MUTE = "MUTE"
VOLUME_UP = "VOLUME_UP"
VOLUME_DOWN = "VOLUME_DOWN"
PRESET_1 = "PRESET_1"
PRESET_2 = "PRESET_2"
PRESET_3 = "PRESET_3"
PRESET_4 = "PRESET_4"
PRESET_5 = "PRESET_5"
PRESET_6 = "PRESET_6"
AUX_INPUT = "AUX_INPUT"
SHUFFLE_OFF = "SHUFFLE_OFF"
SHUFFLE_ON = "SHUFFLE_ON"
REPEAT_OFF = "REPEAT_OFF"
REPEAT_ONE = "REPEAT_ONE"
REPEAT_ALL = "REPEAT_ALL"
PLAY_PAUSE = "PLAY_PAUSE"
ADD_FAVORITE = "ADD_FAVORITE"
REMOVE_FAVORITE = "REMOVE_FAVORITE"

KEYS = [
    PLAY, PAUSE, STOP, PREV_TRACK, NEXT_TRACK, THUMBS_UP, THUMBS_DOWN, BOOKMARK, POWER, MUTE, VOLUME_UP,
    VOLUME_DOWN, PRESET_1, PRESET_2, PRESET_3, PRESET_4, PRESET_5, PRESET_6, AUX_INPUT, SHUFFLE_OFF, SHUFFLE_ON,
    REPEAT_OFF, REPEAT_ONE, REPEAT_ALL, PLAY_PAUSE, ADD_FAVORITE, REMOVE_FAVORITE
]




class BadTouchHttp(object):
    def __init__(self, base_url):
        self._base_url = base_url

    def _resp2dict(self, response):
        log.debug(response.text)
        return xmltodict.parse(response.text, encoding="utf-8")

    def get(self, path):
        return self._resp2dict(requests.get(self._base_url + path))

    def post(self, path, data):
        return self._resp2dict(requests.post(self._base_url + path, data=data))



class BadTouch(object):
    def __init__(self, device, http=BadTouchHttp):
        self._device = device
        self._http = http(base_url="http://{}:8090".format(self._device))

    @cached_property_with_ttl(ttl=5 * 60)
    def info(self):
        return self._http.get("/info")["info"]

    # @key.setter
    def key(self, button):
        button = button.upper()

        log.debug("press {}".format(button))
        self._http.post("/key", data="<key state='press' sender='Gabbo'>{}</key>".format(button))
        log.debug("release {}".format(button))
        self._http.post("/key", data="<key state='release' sender='Gabbo'>{}</key>".format(button))

    def select(self):
        # button = button.upper()

        # log.debug("press {}".format(button))
        self._http.post("/select", data="<ContentItem source='SPOTIFY' type='uri' location='spotify:track:6bRbeEgg8v8BQ0HuVuPE7v' sourceAccount='rishikanthc'></ContentItem>")
        # log.debug("release {}".format(button))
        # self._http.post("/key", data="<key state='release' sender='Gabbo'>{}</key>".format(button))

    def online(self, data):
    	self._http.post("/speaker", data)

# self._http.post("/key", data="<key state='press' sender='Gabbo'>{}</key>".format(button))
data_ol2 = '<play_info><app_key>"string"</app_key><url>http://www.soundjay.com/button/beep-01a.mp3</url><service>"string"</service></play_info>'
data_ol = '<play_info><app_key>"string"</app_key><url>https://ia601504.us.archive.org/17/items/sound_201608.mp3/sound.mp3</url><service>"string"</service></play_info>'

data_ol3 = '<play_info><app_key>"string"</app_key><url>https://archive.org/download/horn.mp3/horn.mp3</url><service>"string"</service></play_info>'
new = '<play_info><app_key>"string"</app_key><url>http://gandalf.ddo.jp/mp3/160807.mp3</url><service>"string"</service></play_info>'

# d = http://www.soundjay.com/button/beep-01a.mp3

sp = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout = 5)
sp.flush()
bt = BadTouch("10.20.5.77")
# bt.online(new)
req = requests.get('http://api.openweathermap.org/data/2.5/weather?q=NewYork&APPID=afad942f01b1f3653c6fe850543048bb')
weath_data = req.json()
print weath_data['weather'][0]['main']
print bt.info
count = 10
# status = score +

while 1:
	recieved = sp.read(2)
	print recieved

	if recieved == 'ON':
		count += 1
		status = "Scoreeee 1 !-!! #BaskLit !" + str(count)
		bt.online(data_ol3)
		# api.update_status("Scoreeee  !!!! #BaskLit !")
		api.update_status(status)
# bt.select()
# bt.key("PLAY")
# bt.key("PAUSE")
# bt.key("NEXT_TRACK")
