# -*- coding: utf-8 -*-
# @Author: chanshub
# @Date:   2018-01-29 23:03:52
# @Last Modified by:   Shubham Chandel
# @Last Modified time: 2018-04-21 06:23:57

import requests

data = {
	'token': "",
	'user': "",
}

JUSTBECAUSE = "Just because I have to put something."

def notify(t, s=JUSTBECAUSE, priority=-1, sound="classical"):
	data['message'] = str(s)
	data['title'] = str(t)
	data['priority'] = priority
	data['sound'] = sound
	r = requests.post('https://api.pushover.net/1/messages.json', data=data)
	print("Notifing", t, s, r)

