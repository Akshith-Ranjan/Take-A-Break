import webbrowser
import time
import random

# list of youtube videos for entertainment during break.
list = ["https://www.youtube.com/watch?v=lK2HwzB-unE",
        "https://www.youtube.com/watch?v=8L1sg7RImyM",
        "https://www.youtube.com/watch?v=CevxZvSJLk8",
        "https://www.youtube.com/watch?v=Cc7yeTxcnvk",
        "https://www.youtube.com/watch?v=WbN0nX61rIs"]
# 10 breaks per day
itirations = 10
# Time between interval 1 hour
interval = 60*60


print "Started working at " + time.strftime('%X %x %Z')
while(itirations):
    time.sleep(interval)
    rand = random.randrange(len(list))
    print "Break at time : " + time.strftime('%X %x %Z')
    webbrowser.open(list[rand])
    itirations = itirations - 1
