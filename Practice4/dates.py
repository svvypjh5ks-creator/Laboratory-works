from datetime import datetime, timedelta
from zoneinfo import ZoneInfo  # Built-in module (Python 3.9+)

#1 Current date and time
now = datetime.now()
print("Current datetime:", now)

#2 Create specific date
specific_date = datetime(2026, 3, 1, 14, 30)
print("Specific date:", specific_date)

#3 Format date
formatted = now.strftime("%d-%m-%Y %H:%M:%S")
print("Formatted date:", formatted)

#4 Time difference (future date)
future = now + timedelta(days=10, hours=5)
difference = future - now
print("Difference in days:", difference.days)
print("Difference in seconds:", difference.seconds)

#5 Calculate difference between two dates
date1 = datetime(2026, 1, 1)
date2 = datetime(2026, 12, 31)
diff = date2 - date1
print("Days between 01-01-2026 and 31-12-2026:", diff.days)