#!/usr/bin/python3.6

import sys
import subprocess

threads = 40

procs = []
logfile = []
for i in range(threads):
    logfile.insert(i, open("logs/log"+str(i)+".txt", 'w'))
    proc = subprocess.Popen([sys.executable, 'pyapp.py'], stdout=logfile[i])
    procs.append(proc)

for proc in procs:
    proc.wait()

for i in range(threads):
    logfile[i].close()
