#!/usr/bin/python
"""
Listen for Facebook messages and add ones which contain an email to a spreadsheet

Sources:
https://www.geeksforgeeks.org/send-message-to-fb-friend-using-python/
http://fbchat.readthedocs.io/en/master/examples.html
"""

import setting
import time
from fbchat import Client, log
from fbchat.models import *
import random
import string
import re
import csv
import setting
import datetime

current_time = '{0:%Y-%m-%d_%H_%M_%S}'.format(datetime.datetime.now())
f1 = open('EmailResponseListings'+current_time+'.csv', 'w')
fieldnames = ['name', 'emails', 'message']
new_email_records = csv.DictWriter(f1, fieldnames=fieldnames)
new_email_records.writeheader()

JIM_PASS = setting.JIM_PASS
JIM_EMAIL = setting.JIM_EMAIL

class StoreMessage(Client):
	def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
		self.markAsDelivered(author_id, thread_id)
		emails = re.findall(r'[\w\.-]+@[\w\.-]+', message_object.text)
		user_name = self.fetchUserInfo(author_id)[author_id].name
		printable_name = ''.join(filter(lambda x: x in string.printable, user_name))
		print(user_name)
		if emails:
			new_email_records.writerow({'name': printable_name, 'emails': emails, 'message': message_object.text})
			self.markAsRead(author_id)
			f1.flush()
		# Unless I'm the author
		if author_id != self.uid:
			log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))
			log.info("{} contains emails: {}".format(message_object.text, emails))

storage = StoreMessage(JIM_EMAIL, JIM_PASS)
storage.listen()
