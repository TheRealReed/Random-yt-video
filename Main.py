import re
import random
import requests
characters = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_'
result = ''
vidstogen = input("[?] How many videos do you want me to genarate?: ")
INCOvids = 0
INCOLISTvids = []
CORRLISTvids = []
CORRvids = 0
def is_valid_youtube_id(video_id):
    checker_url = "https://www.youtube.com/oembed?url=http://www.youtube.com/watch?v="
    video_url = checker_url + video_id

    request = requests.get(video_url)

    return request.status_code == 200
def randomid():
    result = ""
    for i in range (0, 11):
        result += random.choice (characters)
    return result
while CORRvids != int(vidstogen):
    currentvid = randomid()
    if is_valid_youtube_id(currentvid):
        print("[+] Success: Correct Video Produced") # Credit to my dad (for thinking of what to replace "Error" with) [Ryan]
        CORRvids +=1
        CORRLISTvids.append(currentvid)
    else:
        print("[-] Error: Incorrect Video Produced")
        INCOvids +=1
        INCOLISTvids.append(currentvid)
print(f"[+]Here are your vids: {CORRLISTvids} And if you were curios here were the incorrect vids: {INCOLISTvids} AND IF YOURE SUPER MEGA CURIOS Here are the number of incorrect vids and correct vids: {INCOvids} {CORRvids}")





