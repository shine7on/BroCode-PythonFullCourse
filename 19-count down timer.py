import time
import math

my_time = int(input("Enter to your time: "))

'''
# count up
for x in range(1,my_time+1):
    time.sleep(1)
    print(x)
print("Times up")

# count down
for x in range(my_time,0,-1):
    print(x)
    time.sleep(1)

print("Time's Up")
'''


# digital clock
for x in range (my_time,0,-1):
    seconds = x % 60
    minutes = math.floor(x / 60) % 60
    hours = math.floor(x / 3600)

    time.sleep(1)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
print("Time's Up")
