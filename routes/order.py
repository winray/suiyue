import time

def get_order():
    s = "2016-06-05 00:00:00"
    start = time.mktime(time.strptime(s,"%Y-%m-%d %H:%M:%S"))
    stime = time.time() - start
    order = int(stime/604800)+1
    return order