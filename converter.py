
import time    

from datetime import datetime

now = time.time()

print(now)

dt = datetime.fromtimestamp( now )

d = dt.strftime("%m/%d/%Y, %H:%M:%S")

print(d.replace(", ", "T").replace("/", "-", 2)+'Z')

