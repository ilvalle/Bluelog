import os.path
import datetime
from datetime import timedelta
import requests

fname="/tmp/last_ts_online"
if os.path.isfile(fname):
    print 'esiste'
    with open(fname, 'r') as f:
        lines = f.readlines()
        current_ts = datetime.datetime.now()
        last_ts = datetime.datetime.strptime(lines[0], "%Y-%m-%d %H:%M:%S") 
        diff = current_ts - last_ts
        if diff > timedelta(hours=6):
            command = "/usr/bin/sudo /sbin/shutdown -r now"
            import subprocess
            process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
            output = process.communicate()[0]

try:
    r = requests.head('http://www.google.it', timeout=5)
    if r.status_code == 200:
        with open(fname, 'w') as f:
            f.write("%s" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))        
except:
    print 'non aggiorno'
    pass
