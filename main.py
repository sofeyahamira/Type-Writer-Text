import sys, time

# type writer function
def write(message):
  for char in message:
    sys.stdout.write(char)
    sys.stdout.flush()

    if char != '\n':
      time.sleep(0.05)
    else:
      time.sleep(0.5)