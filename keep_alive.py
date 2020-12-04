from flask import Flask
#from threading import Thread
from termcolor import colored as cl
import random
import string
import requests, os
import time as t

def get_random_string(length):
    random_list = []
    for i in range(length):
      random_list.append(random.choice(string.ascii_uppercase + string.digits))
    return ''.join(random_list)
length = [5, 6, 7]
randomSet = get_random_string(random.choice(length)).lower()

#set flask app name
name = input('flask app name (leave blank for random): ')
if name == "":
  name = randomSet
route = input('flask route location (leave blank for random): ')
#set flask app route
if route == "":
  route = randomSet
elif route.isalpha() == False:
  print(cl('your route cannot be ' + route, 'magenta'))
  t.sleep(2)
  os.system('python3 keep_alive.py')
  
#set flask return content
website = input('website to grab (without http/https): ')
if website == "":
  print(cl('website cannot be blank', 'magenta'))
  t.sleep(2)
  os.system('python3 keep_alive.py')
website = 'http://' + website
cont = requests.get(website)
cont = cont.content
content = cont

app = Flask(name)

@app.route('/' + route)
def main():
  return content

@app.route('/')
def index():
  return "<center><p>and i oop-</p><br><br><a href='/" + route + "'>your route</a></center>"

def run():
  app.run(host="0.0.0.0", port=0)
print(cl('starting your hydroflask...', 'cyan'))
print(cl('started at: 0.0.0.0/' + route, 'green'))
t.sleep(2)
run()