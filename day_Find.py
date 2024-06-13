import datetime

def day_of_the_week(year, month, day):
    try:
        date_obj = datetime.date(year, month, day)
        weekday_index = date_obj.weekday()
        weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

        return weekdays[weekday_index]
    except ValueError:
        return "Invalid Input"

year = int(input("Enter the Year (XXXX): "))
month = int(input("Enter the Month (XX): "))
day = int(input("Enter the date (XX): "))

result = day_of_the_week(year, month, day)
print(f"The day of the week for {year}-{month}-{day} is {result}")
