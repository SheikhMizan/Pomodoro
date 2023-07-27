from playsound import playsound
import time

duration = int(input('Enter Duration for your Pomodoro in minutes: '))

print(time.asctime())
print('Pomodoro Started. Focus....')
for i in range(10):
    playsound('TickTick.mp3')
    #Giving 0.8 as argument works best
    time.sleep(0.8)

print('Pomodoro Completed!')
playsound('Alarm.mp3')
