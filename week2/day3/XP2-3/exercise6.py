# 🌟 Exercise 6: Birthday and minutes
# Key Python Topics:

# datetime module
# datetime.datetime.strptime() (parsing dates)
# Time difference calculations
# .total_seconds() method


# Instructions:

# Create a function that accepts a birthdate as an argument (in the format of your choice), then displays a message stating how many minutes the user lived in his life.


import  datetime

def lived_minutes(year, month, day):
    current_time =  datetime.datetime.now()
    birthday = datetime.datetime(year, month, day)
    age = current_time - birthday
    age_minutes = age.total_seconds() / 60
    return round(age_minutes)

print(f'Your age in minutes: {lived_minutes(1991, 4, 13)}')
