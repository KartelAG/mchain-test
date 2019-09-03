#!/usr/bin/python3.6

import sys
import subprocess

procs = []
for i in range(20):
    proc = subprocess.Popen([sys.executable, 'pyapp.py'])
    procs.append(proc)

for proc in procs:
    proc.wait()
