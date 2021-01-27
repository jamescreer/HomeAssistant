import datetime

today = datetime.date.today()
if today.weekday() > 1:
	# If this Thursday has passed, we only care about next week.
	today = today + datetime.timedelta((0 - today.weekday()) % 7)

# Get the ISO week number (1-52~53)
week_number = today.isocalendar()[1]

if (week_number % 2) == 0:
	# Even weeks are for Landfill waste
	collection_type = 'Organics & Recycling'
else:
	# Odd weeks are for Recycling and Garden Waste.
	collection_type = 'Organics & Landfill'

print(collection_type)