import time
from datetime import date
from datetime import datetime
from datetime import timedelta
import locale

locale.setlocale(locale.LC_ALL, 'ru_RU')
print(date.today())
print(datetime.now())
timer = datetime.now() + timedelta(seconds=1.0001)
print('time now - ', '\t', datetime.now())
print('time + 1 sec', '\t', timer)
# for i in timer:
#     sec=datetime.now().strftime('%c').capitalize()
#     print(sec)
while timer >= datetime.now():
    # print(datetime.now())
    continue
print('time stop ', '\t' * 2, datetime.now())
time.sleep(1)
print('time stop ', '\t' * 2, datetime.now())

print('data:', datetime.now().strftime('%A %d %Y').capitalize())
print('time:', datetime.now().strftime('%H:%M:%S').capitalize())
