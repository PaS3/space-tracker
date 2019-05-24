#!/usr/bin/python3
import random
import urllib as ul
import urllib.request as ulrqst

import json 

import tkinter as tk
from tkinter import * 


      
# set inititial cords 
print("What are your GPS cordinates?")
lat = str(input("Latitude  > "))
lon = str(input("Longitude > "))

if len(lat) == 0 or len(lon) == 0:
  lat = str(45.9647393)
  lon = str(63.3037767)

iss_now_data_url = "http://api.open-notify.org/iss-now.json"
iss_pass_data_url = "http://api.open-notify.org/iss-pass.json?lat=" + lat + "&lon=" + lon  
iss_crew_data_url = "http://api.open-notify.org/astros.json"


from datetime import datetime

with ul.request.urlopen(iss_now_data_url) as iss_now_data:
     iss_now = json.loads(iss_now_data.read().decode('utf-8'))
     print("\nThe ISS current location at \033[32m", datetime.utcfromtimestamp(iss_now['timestamp']).strftime('%H:%M:%S %Y-%m-%d ') ,"\033[0mis\033[31m ", iss_now['iss_position'] ,"\033[0m.\n ")

with ul.request.urlopen(iss_pass_data_url) as iss_pass_data:
     iss_pass = json.loads(iss_pass_data.read().decode('utf-8'))
     for rise_period in iss_pass['response']: 
        print("\nThe ISS will be overhead {\033[31m",
              iss_pass['request']['latitude'], "\033[0m,\033[31m",
              iss_pass['request']['longitude'] , "\033[0m} at\033[31m",
              datetime.utcfromtimestamp(rise_period['risetime']).strftime('%H:%M:%S %Y-%m-%d '),
              "\033[0m for\033[31m",
              datetime.utcfromtimestamp(rise_period['duration']).strftime('%H:%M:%S'),
              "(Hr:Min:Sec)\033[0m.\n")


with ul.request.urlopen(iss_crew_data_url) as iss_crew_data:
      iss_crew = json.loads(iss_crew_data.read().decode('utf-8'))
      sum_all_crew = iss_crew['number']
      craft_array = []
      count = int()
      for crew_row in range(0,sum_all_crew):
        if iss_crew['people'][crew_row]['craft'] not in craft_array:
          count = count + 1
          craft_array.append( [ iss_crew['people'][crew_row]['craft'], iss_crew['people'][crew_row]['name'], count ])
      sum_of_crew = len(craft_array)
      print("\n There are\033[31m", sum_of_crew,"\033[0m people aboard the \033[31m",craft_array[1][0],"\033[0m.They are")
      for crafts in craft_array:
        print("\nName:\033[31m", crafts[1],"\033[0m\t\t\tCrew #:\033[31m ", crafts[2],"\033[0m\n ")


input("Reload?")



















