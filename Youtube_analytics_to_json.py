import urllib.request
from datetime import datetime
import json
import subprocess
import keyboard
import time



name = input("enter id:     ")

key = "AIzaSyBNb4u9GmM9pgzKArHyEaW-p-nAIskVJCU"

data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id="+name+"&key="+key).read()
subs=json.loads(data)["items"][0]["statistics"]["subscriberCount"]
views=json.loads(data)["items"][0]["statistics"]["viewCount"]

now = datetime.now().time()

current_time = now.strftime("%H:%M:%S")

print("subscribers:     "+subs+"    views:    "+views+"     time:    "+current_time)


data = []

def json_writing():
    # Data to be written

    a_dictionary = {
    "subs" : subs,
    "views" : views,
    "time" : current_time
    }

    with open("data.json") as outfile:
        data = json.load(outfile)
        data.append(a_dictionary)
        outfile.close()
    with open("data.json", "w") as outfile:
        json.dump(data, outfile, indent = 2)
        outfile.close()


def Ram_update():
    global subs_Ram
    global views_Ram

    subs_Ram = subs
    views_Ram = views

Ram_update()

a_dictionary = {
"subs" : subs,
"views" : views,
"time" : current_time
}

with open("data.json") as outfile:
    data.append(a_dictionary)
with open("data.json", "w") as outfile:
    json.dump(data, outfile, indent = 2)
    outfile.close()



while True:

    data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id="+name+"&key="+key).read()
    subs=json.loads(data)["items"][0]["statistics"]["subscriberCount"]
    views=json.loads(data)["items"][0]["statistics"]["viewCount"]


    if  subs_Ram != subs or int(views_Ram) >= (int(views) + 10):
        now = datetime.now().time()

        current_time = now.strftime("%H:%M:%S")

        print("subscribers:     "+subs+"    views:    "+views+"     time:    "+current_time)
        time.sleep(3)
        Ram_update()
        json_writing()

    if keyboard.is_pressed('esc'):
        break

subprocess.call("Json_to_graph_conv.py", shell=True)