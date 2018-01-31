#!/usr/bin/python
"""
Get list of message users for specific Facebook account using fbchat
"""
# https://www.geeksforgeeks.org/send-message-to-fb-friend-using-python/
# http://fbchat.readthedocs.io/en/master/examples.html
import setting
import time
from fbchat import Client
from fbchat.models import *
import random
 
## Get the IDs of non-friends in group
import csv
f1 = open('GroupNonFriends.csv', 'r')

group = csv.reader(f1)

# Make a list of the IDs of the Members who aren't found as friends.
IDs = []
for row in group:
	IDs.append(row[0])

# Make a note here of when users were messaged
messaged = {}

JIM_PASS = setting.JIM_PASS
JIM_EMAIL = setting.JIM_EMAIL

client = Client(JIM_EMAIL, JIM_PASS)

print("Getting Session")
session_cookies = client.getSession()
client.setSession(session_cookies)

if not client.isLoggedIn():
    client.login(JIM_EMAIL, JIM_PASS, session_cookies=session_cookies)

users = client.fetchAllUsers()


f2 = open('MessageRecords.csv', 'w')
fieldnames = ['id', 'name', 'message result']
message_records = csv.DictWriter(f2, fieldnames=fieldnames)
message_records.writeheader()
count = 0
for user in users:
	if user.uid in IDs:
		pause = random.uniform(5, 12)
		count += 1
		if (500 % count = 0):
			pause = random.uniform(5, 12)
		print("Sending message to: {}".format(user.name))
		# time.sleep(pause)
		messaged[user.uid] = client.send(Message(text='Hi '+user.first_name+'. We\'re bla bla bla. Please send me your email or signup at http://eepurl.com/dhtmDL.'), thread_id=user.uid, thread_type=ThreadType.USER)
		message_records.writerow({'id': user.uid, 'name': user.name, 'message result': messaged[user.uid]})
client.logout()
