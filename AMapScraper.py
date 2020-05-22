import urllib.request
import json
import os
import time
from math import floor
import random

originaltime = time.time()
Waittime = random.randint(10, 59)
while True:
    times = time.time()
    urls = "https://umap.openstreetmap.fr/en/datalayer/1284705/"
    with urllib.request.urlopen(urls) as url:
        with open("DataLayer.json", "r", encoding = "UTF-8") as fileold:
            data = json.load(fileold)
            datanew = json.loads(url.read().decode())
            print("Checked at " + str(time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(times))))
            if not (data == datanew):
                datetime = str(time.strftime('%d-%m-%Y_%H-%M-%S', time.localtime(times)))
                Waittime = random.randint(10, 59)
                print("Change detected: ")
                print("Old file: " + str(len(data["features"])) + " entries")
                print("New file: " + str(len(datanew["features"])) + " entries")
                with open("DataLayer_" + datetime + ".json", "w", encoding = "UTF-8") as outfile:
                    json.dump(data, outfile)
                with open("DataLayer.json", "w", encoding = "UTF-8") as outfile:
                    json.dump(datanew, outfile)
            else:
                Waittime = (Waittime + random.randint(0, 180)) * 2
                if Waittime > 7200:
                    Waittime = 7200
    if time.time() - times <= Waittime:
        if Waittime < 60:
            print("Current wait time: " + str(Waittime) + " seconds")
        else:
            Minutes = floor(Waittime/60)
            Seconds = round(Waittime%60)
            if Minutes < 60:
                print("Current wait time: " + str(Minutes) + " minutes " + str(Seconds) + " seconds" )
            else:
                Hours = floor(Minutes/60)
                Minutes = Minutes%60
                print("Current wait time: " + str(Hours) + " hours " + str(Minutes) + " minutes " + str(Seconds) + " seconds" )
        time.sleep(Waittime - (times - time.time()))
    worktime = round(time.time() - originaltime)
    if worktime < 60:
        print("Working for " + str(worktime) + " seconds")
    else:
        Seconds = worktime % 60
        Minutes = floor(worktime/60)
        if Minutes > 60:
            hours = floor(Minutes / 60)
            Minutes = Minutes % 60
            print("Working for " + str(hours) + " hours " + str(Minutes) + " minutes " + str(Seconds) + " seconds")
        else:
            print("Working for " + str(Minutes) + " minutes " + str(Seconds) + " seconds")
        
    
