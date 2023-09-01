import json
import requests
import os
import time
import schedule



# load config
with open('/config/config.json', 'r') as f:
    config = json.load(f)
username = config['username']
password = config['password']
telegramtoken = config['telegramtoken']
telegramchatid = config['telegramchatid']
enabletelegram = config['enabletelegram']


downloadpath = "/downloads/"


def clean_filename(filename): # clean filename for writing
    for ch in ['\\', '/', ':', '*', '?', '"', '<', '>', '|']:
        if ch in filename:
            filename = filename.replace(ch, '')
    return filename

def get_streamable_videos_link(username,password): # get new streamable video link and data
    links=[]
    print("conecting to streamable account")
    session = requests.Session()
    print("getting videos count")
    session.post('https://ajax.streamable.com/check', json={"username": username, "password": password},headers={"Content-Type": "application/json"})
    response = session.get('https://ajax.streamable.com/api/v1/videos')
    data = response.json()
    if data['total'] == 0:
            print('No videos found...')
    for index in range(1, (data['total'] // 100) + 2):
        print(f"getting videos list {index}")
        videos_response = session.get(f'https://ajax.streamable.com/api/v1/videos?sort=date_added&sortd=DESC&count=100&page={index}')
        videos = videos_response.json()
        for video in videos['videos']:
            if check_is_present_to_DB(video["url"].split("/")[-1]):
                print(f'video already present to DB : {video["url"].split("/")[-1]}')
            else:
                print(f'getting video info : {video["url"].split("/")[-1]}')
                video_resp = requests.get(f'https://api.streamable.com/videos/{video["url"].split("/")[-1]}')
                videodata=video_resp.json()
                filename= videodata['title']+"_"+ video["url"].split("/")[-1] + ".mp4"
                url = videodata['files']['mp4']['url']
                tag = video["url"].split("/")[-1]
                links.append((url,filename,tag))
                f = open("/config/DB.txt","a") # add to DB
                f.write(tag+"\n")
                f.close()
    print("streamable videos links extraction finished")
    return links

def download_vid(url,filename):
    print(f"downloading : {filename}")
    videofile = requests.get(url)
    with open(downloadpath+clean_filename(filename), 'wb') as f:
        f.write(videofile.content)
    print("download finished")

def check_is_present_to_DB(tag):
    f = open("/config/DB.txt","r")
    DB = f.read().split("\n")
    f.close()
    for line in DB:
        if tag in line:
            return True
    return False

def main () :
    print("START")
    # get new streamable videos links
    links = get_streamable_videos_link(username,password)

    # download videos
    for url,filename,tag in links:
        download_vid(url,filename)

    if enabletelegram:
        # send to telegram
        tmp = list(os.scandir(downloadpath))
        for filename in tmp:
            print(f"uploading to telegram: {filename.path}")
            file = {'document': open(filename.path, 'rb')}
            res = requests.post(f'https://api.telegram.org/bot{telegramtoken}/sendDocument?chat_id={telegramchatid}', files=file)
            print("upload finished")

            # delete file after upload
            print(f"deleting file: {filename.path}")
            os.remove(filename.path)
            print("delete finished")

    print("END")

if __name__ == "__main__":
    print("streamable-archiver started")
    main()
    schedule.every().day.at("01:00", "Europe/Paris").do(main)
    while True:
        schedule.run_pending()
        time.sleep(1)
