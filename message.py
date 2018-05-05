#!/usr/bin/python
"""
Send intermittent message to all members of a Facebook Group
I got the Group Member IDs and Names using the Node package:
https://www.npmjs.com/package/facebook-export

https://www.geeksforgeeks.org/send-message-to-fb-friend-using-python/
http://fbchat.readthedocs.io/en/master/examples.html
"""

import setting
import time
from fbchat import Client
from fbchat.models import *
import random
import datetime
 
## Get the IDs of non-friends in group
import csv
f1 = open('GroupMembers.csv', 'r')

group = csv.reader(f1)

# Make a note here of when users were messaged
messaged = {}

USER_PASS = setting.JOHN_PASS
USER_EMAIL = setting.JOHN_EMAIL

client = Client(USER_EMAIL, USER_PASS)

print("Getting Session")
session_cookies = client.getSession()
client.setSession(session_cookies)

if not client.isLoggedIn():
    client.login(USER_EMAIL, USER_PASS, session_cookies=session_cookies)

current_time = '{0:%Y-%m-%d_%H_%M_%S}'.format(datetime.datetime.now())
# Record Response Results in a file that won't be accidentally overwritten
f2 = open('MessageRecords'+current_time+'.csv', 'w')
fieldnames = ['id', 'name', 'message result']
message_records = csv.DictWriter(f2, fieldnames=fieldnames)
message_records.writeheader()
count = 0
for user in group:
	pause = random.uniform(60, 215)
	count += 1
	try: 
		print("Sending message to: {} {}".format(user[1], user[2]))
		time.sleep(pause)
		messaged[user[0]] = client.send(Message(text='Hi '+user[1]]+'. You are beautiful. We\'re making an email list for Shanti Wasi Medicine Nights. I\'ll add you if you send back your email.'), thread_id=user[0], thread_type=ThreadType.USER)
		message_records.writerow({'id': user.uid, 'name': user.name, 'message result': messaged[user.uid]})
		# Write out to the file
		f1.flush()
	except FBchatFacebookError as e:
		message_records.writerow({'id': 'user.uid', 'name': user.name, 'message result': 'ERROR: ' + str(e)})
		# Wait a long time
		pause = random.uniform(212350, 22610)
		f1.flush()
client.logout()
