import datetime
import time
import winsound  # Only works on Windows

def get_alarm_time():
    while True:
        try:
            alarmHour = int(input("Enter hour (1-12): "))
            if not (1 <= alarmHour <= 12):
                raise ValueError
            alarmMin = int(input("Enter minute (0-59): "))
            if not (0 <= alarmMin <= 59):
                raise ValueError
            alarmAMPM = input("AM/PM: ").strip().lower()
            if alarmAMPM not in ['am', 'pm']:
                raise ValueError
            return alarmHour, alarmMin, alarmAMPM
        except ValueError:
            print("Invalid input. Please enter the correct time and format.")

# Get alarm time from the user
alarmHour, alarmMin, alarmAMPM = get_alarm_time()

# Convert to 24-hour time if needed
if alarmAMPM == 'pm' and alarmHour != 12:
    alarmHour += 12
elif alarmAMPM == 'am' and alarmHour == 12:
    alarmHour = 0

print(f"Alarm set for {alarmHour:02}:{alarmMin:02}")

# Loop until the alarm time
while True:
    now = datetime.datetime.now()
    currentHour = now.hour
    currentMinute = now.minute

    if alarmHour == currentHour and alarmMin == currentMinute:
        print("Playing alarm sound...")
        winsound.PlaySound("alarm.wav", winsound.SND_FILENAME)
        break
    
    time.sleep(10)  # Wait for 10 seconds before checking again
