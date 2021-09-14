# MultiPurpose Discord Bot

## About
This bot is made using discord.py, no cogs are used so its beginner friendly.

## Install Packagaes 
```bash
import discord
from discord.ext import commands
import time
import os
import random
import json
from PIL import Image
from io import BytesIO
import traceback

import aiohttp
```

## How to use ? 
Just clone the repository change ur token and run it. (Do install all the packages)

## Can I publish the bot ? 
You cant.... 

## I want to host it 24/7 for free

You can host it 24/7 simply from [repl.it](https://replit.com/~)

### Step 1 to host 
Go to [repl.it](https://replit.com/~)
sign up and login 

### Step 2
Create a new repl 
![Create_repl](https://media.discordapp.net/attachments/736596667184185524/887264666609393685/unknown.png?width=233&height=182)


### Step 3
Select Python and Create repl
![Select_Python](https://media.discordapp.net/attachments/736596667184185524/887265239505207306/unknown.png?width=541&height=396)

### Step 4 
Copy whole main.py code in main.py 

now create a file `webserver.py`
and paste this code there

```py
from flask import Flask
from threading import Thread
import random


app = Flask('')

@app.route('/')
def home():
    return 'Webserver is working !'

def run():
  app.run(
        host='0.0.0.0',
        port=random.randint(2000,9000)
    )

def keep_alive():
    '''
    Creates and starts new thread that runs the function run.
    '''
    t = Thread(target=run)
    t.start()
```

### Step 5

Make a scret key 

![create_secret](https://media.discordapp.net/attachments/736596667184185524/887266538841866280/unknown.png?width=216&height=497)

Set Key as TOKEN 
and value as token of your bot

### Step 6
Replace 
```py
client.run
```
with 
```py
keep_alive()
  
  

client.run(os.getenv('TOKEN'))  
```
and import the file 
```py
from webserver import keep_alive
```

## We've succesfully created a web server 

### Step 7
Go to [uptimerobott](https://uptimerobot.com/)

Sign Up Login 

add a monitor 
![add_monitor](https://media.discordapp.net/attachments/736596667184185524/887267831127887903/unknown.png?width=369&height=85)

Copy this link from replit 
![copy_link](https://media.discordapp.net/attachments/736596667184185524/887268090730131456/unknown.png?width=533&height=314)

Apply these settings and deploy monitor
![settings](https://media.discordapp.net/attachments/736596667184185524/887268655933554688/unknown.png?width=613&height=303)

# Congratulations you just hosted your bot 24/7
