import pytz
from _pydatetime import datetime

data = datetime.now(pytz.timezone("Europa/Oslo"))
print(data)

