#FutureTime.py
#Name: Ryan Meegan
#Date: Feb 2 2025
#Assignment: Future Time

# datetime will allow us to access the system date and time.
import datetime
import pytz
central_tz = pytz.timezone("America/Chicago")

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now(central_tz)
  currentHour = now.hour 
  currentMinute = now.minute

  print("Current time:", f"{currentHour:02}:{currentMinute:02}")

  #TODO:
  #Ask user for hours
  hoursToAdd = int(input("Enter hours to add: "))

  #Ask user for minutes
  minutesToAdd = int(input("Enter minutes to add: "))

  totalMinutes = currentMinute + minutesToAdd
  futureMinutes = totalMinutes % 60
  extraHours = totalMinutes // 60

  totalHours = currentHour + hoursToAdd + extraHours
  futureHour = totalHours % 24

  print(f"Future time: {futureHour:02}:{futureMinutes:02}")

if __name__ == '__main__':
  main()
