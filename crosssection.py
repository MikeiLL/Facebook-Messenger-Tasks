#!/usr/bin/python
"""
Compare two small csv files and create two new files, one with matches, the other which don't match.

I use it here to to get the names and email addresses from a specific group who are "personal" FB friends.
It loops the group and pulls matches from the friends list, so that only group members whom are also found in the 
friends list will be included in the GroupFriends list.

A hipper, more efficient approach is found here: https://stackoverflow.com/a/23090697/2223106
"""

import csv

f1 = file('FBGroupMembers.csv', 'r')
f2 = file('FBFriends.csv', 'r')
f3 = file('GroupFriends.csv', 'w')
f4 = file('GroupNonFriends.csv', 'w')

group_reader = csv.reader(f1)
friends_reader = csv.reader(f2)
crosssection_writer = csv.writer(f3)
non_match_writer = csv.writer(f4)

friend_list = list(friends_reader)

for group_row in group_reader:
	row = 1
	found = False
	for friends_row in friend_list:
		# If first or last name matches we at least have an email for a member of the group, even if not the correct first name
		if friends_row[0].lower() == group_row[1].lower() or friends_row[3].lower() == group_row[2].lower():
			friends_row[0] = friends_row[0].title()
			friends_row[3] = friends_row[3].title()
			print(friends_row[0] +'\t'+friends_row[3]+' found.')
			friends_row.append(group_row[0])
			crosssection_writer.writerow(friends_row)
			found = True
			break
		row = row + 1
	if not found:
		group_row.append(group_row[0])
		non_match_writer.writerow(group_row)

f1.close()
f2.close()
f3.close()
f4.close()