#!/usr/local/bin/python3

# 자신만의 시각 알림 서비스

# 입력: 현재 시각
# 프로세스: 현재 시각을 웹에 json 형태로 올린다
# 출력: 웹에서 현재 시각을 가져와 출력한다

import urllib.request
import json

def number_to_month(number):
	month_names = {'1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May', '6': 'June', '7': 'July', '8': 'August', '9': 'September', '10': 'October', '11': 'November', '12': 'December'}
	month = month_names[number]
	return month

message = "The current time is {}."

url = "http://127.0.0.1:8008/time"

time_json = urllib.request.urlopen(url).read().decode("utf-8")
time_dict = json.loads(time_json)
current_time = time_dict["current_time"]
time = current_time[11:]
month_number = current_time[5:7]
day = current_time[8:10]
year = current_time[:4]
result = "{} UTC {} {} {}".format(time, number_to_month(month_number), day, year)

print(message.format(result))
