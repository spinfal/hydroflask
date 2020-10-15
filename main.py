import os
from termcolor import colored as cl
import time as t

print(cl('this might not work unless you are running this at https://repl.it/@spinfal/hydroflask', 'red'))
t.sleep(3)

print(cl('starting...', 'green'))
os.system('python3 keep_alive.py')