from datetime import date, datetime

def days_btwn(d1, d2):
    diff = d2-d1
    return diff.days

date1 = date(2024, 3, 1)
date2 = date(2024, 3, 10)

curr_timestamp = datetime.now()

print("Date Example: ")
print("Date 1:", date1)
print("Date 2:", date2)

print("\nTimestamp Example: ")
print("Current Timestamp:", curr_timestamp)

diff = days_btwn(date1, date2)

print("\nDifference in days:", diff)

