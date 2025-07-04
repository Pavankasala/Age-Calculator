import time
from calendar import isleap

# ----------- Helper function to get number of days in a month -----------
def get_days_in_month(month, is_leap):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if is_leap else 28

# ----------- Step 1: Take user input -----------
print("==== Age Calculator ====")
name = input("Enter your name: ")
birth_year = int(input("Enter your birth year (e.g., 2001): "))
birth_month = int(input("Enter your birth month (1-12): "))
birth_day = int(input("Enter your birth day (1-31): "))

# ----------- Step 2: Get current date from system -----------
current_time = time.localtime()
current_year = current_time.tm_year
current_month = current_time.tm_mon
current_day = current_time.tm_mday

# ----------- Step 3: Calculate total years lived -----------
years = current_year - birth_year

# If birthday hasn't occurred yet this year, subtract 1 year
if (current_month < birth_month) or (current_month == birth_month and current_day < birth_day):
    years -= 1

# ----------- Step 4: Calculate total months lived -----------
months = (current_year - birth_year) * 12 + (current_month - birth_month)

# If day hasn't passed in current month, subtract 1 month
if current_day < birth_day:
    months -= 1

# ----------- Step 5: Calculate total days lived -----------
total_days = 0

# a) Count full days from birth year to current year (excluding start and end years)
for year in range(birth_year + 1, current_year):
    total_days += 366 if isleap(year) else 365

# b) Count remaining days in birth year
if birth_year != current_year:
    is_leap_birth = isleap(birth_year)

    # Add days left in birth month
    total_days += get_days_in_month(birth_month, is_leap_birth) - birth_day

    # Add days in remaining months of birth year
    for m in range(birth_month + 1, 13):
        total_days += get_days_in_month(m, is_leap_birth)

# c) Add days in current year up to today
is_leap_current = isleap(current_year)

# Add days in full months of current year before current month
for m in range(1, current_month):
    total_days += get_days_in_month(m, is_leap_current)

# Add days passed in current month
total_days += current_day

# d) If born this year, subtract days before birth
if birth_year == current_year:
    is_leap_current = isleap(current_year)
    
    # Subtract days before birth month
    for m in range(1, birth_month):
        total_days -= get_days_in_month(m, is_leap_current)
    
    # Subtract days before birth day
    total_days -= (birth_day - 1)

# ----------- Step 6: Show the result -----------
print("\n==== Result ====")
print(f"{name}'s age is:")
print(f"➡️ {years} years")
print(f"➡️ {months} months (approximate)")
print(f"➡️ {total_days} days (exact)")
