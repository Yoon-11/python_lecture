import time
currentTime = time.time()

totalSeconds = int(currentTime)
currentSecond = totalSeconds % 60

totalMinutes = totalSeconds // 60
currentMinutes = totalMinutes % 60

totalHours = totalMinutes // 60
currentHours = totalHours % 24

print(currentSecond, currentMinutes, currentHours)
