thatDay = "2022-8-24"
from datetime import datetime,timedelta
theDay = datetime.strptime(thatDay, "%Y-%m-%d").date()

# And then I push 120 days + timedelta(days=120)
target = theDay + timedelta(days=120)

print(target)
print(target.weekday())

# And then I push 120 days - timedelta(days=120)
target = theDay - timedelta(days=120)

print(target)
print(target.weekday())
