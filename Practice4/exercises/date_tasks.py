from datetime import datetime, timedelta

#1 Subtract five days from current date
now = datetime.now()
five_days_ago = now - timedelta(days=5)
print("Five days ago:", five_days_ago)

#2 Yesterday, Today, Tomorrow
today = datetime.now().date()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

#3 Drop microseconds
no_microseconds = now.replace(microsecond=0)
print("Without microseconds:", no_microseconds)

#4 Difference between two dates in seconds
date1 = datetime(2026, 1, 1)
date2 = datetime(2026, 1, 2)

difference = date2 - date1
print("Difference in seconds:", difference.total_seconds())