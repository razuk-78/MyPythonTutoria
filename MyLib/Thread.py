import threading
import time
def fun(*data:str):
   while True:
       #sleep
       time.sleep(2)
       print(data[0])
       threading.Thread.
th = threading.Thread(group=None, target=fun, name="test", args=("data","datab"), kwargs={}, daemon=None)

th.start()
