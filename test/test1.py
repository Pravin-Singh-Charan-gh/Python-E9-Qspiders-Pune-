import time

_time = int(input(('Enter the time in seconds : ')))

for x in reversed(range(_time+1)):
    seconds = _time%60
    minutes = (_time//60)%60
    hours = _time//3600
    print(f'{hours:02}:{minutes:02}:{seconds:02}')
    time.sleep(1)
    _time-=1

print('Time is Up!')