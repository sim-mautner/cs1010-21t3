# A function which takes a month and day of the year,
# and returns the number of days into the year.
def days_into_year(month, day):
    total = day
    if month > 0:
        total += 31
    if month > 1:
        total += 28
    if month > 2:
        total += 31
    if month > 3:
        total += 30
    if month > 4:
        total += 31
    if month > 5:
        total += 30
    if month > 6:
        total += 31
    if month > 7:
        total += 30
    if month > 8:
        total += 31
    if month > 9:
        total += 30
    if month > 10:
        total += 31
    return total

# Function which prints out a couple test values of days_into_year
def quickTest():
    print(f"month 0, day 0 = {days_into_year(0,0)}")
    print(f"month 11, day 31 = {days_into_year(11,31)}")

#if __name__ == '__main__':
#    quickTest()

quickTest()