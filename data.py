from datetime import date
from datetime import datetime
from datetime import timedelta
import locale
locale.setlocale(locale.LC_ALL, 'ru_RU')
print(date.today())
print(datetime.now())
# dn = datetime.now().strftime('%A')
timer=datetime.now()+timedelta(seconds=3)
print('test - ', datetime.now(''))
print('test - ', timer)
# for i in timer:
#     sec=datetime.now().strftime('%c').capitalize()
#     print(sec)
# while datetime.now() != timer:
#     print(datetime.now())


print('data:', datetime.now().strftime('%A %d %Y').capitalize())
print('time:', datetime.now().strftime('%H:%M:%S').capitalize())

