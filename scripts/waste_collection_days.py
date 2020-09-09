import datetime
import json

today = datetime.date.today()
currentday = datetime.date.today()
# Normal collection day is Thursday, day 3 of a zero-indexed week.
if today.weekday() > 0:
	# If this Thursday has passed, we only care about next week.
	today = today + datetime.timedelta((0 - today.weekday()) % 7)

# Set the collection date to next Thursday.    
next_collection = today + datetime.timedelta((0 - today.weekday()) % 7) 
delta = next_collection - currentday
print(delta.days)