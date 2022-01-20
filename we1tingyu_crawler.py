import requests
import time
import os
import json

url = 'https://api.lolicon.app/setu/v2'
download_num = 30

def download(num):
    for i in range(0, num):
        r = requests.get(url)
        dic = r.json()

        pic_title = dic["data"][0]["title"]
        pic_url = dic["data"][0]["urls"]["original"]
        pic_pid = dic["data"][0]["pid"]
        pic_author = dic["data"][0]["author"]
        pic_filename = str(pic_pid) + "_" + pic_title + \
            "_" + pic_author + ".png"
        os.system("wget -nv " + pic_url + " -O \"pic/" +
                  pic_filename + "\" --connect-timeout 2 --no-check-certificate --user-agent=\"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0\"")
        time.sleep(1)
