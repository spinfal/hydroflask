from flask import Flask
#from threading import Thread
from termcolor import colored as cl
from random_word import RandomWords
import requests, os
import time as t
r = RandomWords()

randomSet = r.get_random_word()
#set flask app name
name = input('flask app name (leave blank for random): ')
if name == "":
  name = randomSet
route = input('flask route location (leave blank for random): ')
#set flask app route
if route == "":
  route = randomSet
elif route.isalpha() == False:
  print(cl('your route cannot contain the character ' + route, 'magenta'))
  t.sleep(2)
  os.system('python3 keep_alive.py')
  
#set flask return content
website = input('website to grab: ')
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

def run():
  app.run(host="0.0.0.0", port=0)
print(cl('starting your hydroflask...', 'cyan'))
print(cl('started at: 0.0.0.0/' + route, 'green'))
t.sleep(2)
run()
