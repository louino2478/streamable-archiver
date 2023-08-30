import json
import requests

with open('config.json', 'r') as f:
    config = json.load(f)
username = config['username']
password = config['password']
downloadpath = "downloads/"


def clean_filename(filename):
    for ch in ['\\', '/', ':', '*', '?', '"', '<', '>', '|']:
        if ch in filename:
            filename = filename.replace(ch, '')
    return filename

def get_streamable_videos_link(username,password):
    links=[]
    print("conecting to streamable acount")
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
            print(f'getting video info : {video["url"].split("/")[-1]}')
            video_resp = requests.get(f'https://api.streamable.com/videos/{video["url"].split("/")[-1]}')
            videodata=video_resp.json()
            filename= videodata['title']+"_"+ video["url"].split("/")[-1] + ".mp4"
            url = videodata['files']['mp4']['url']
            tag = video["url"].split("/")[-1]
            links.append((url,filename,tag))
    print("streamable videos links extraction finished")
    return links

def download_vid(url,filename):
    print(f"downloading : {filename}")
    videofile = requests.get(url)
    with open(downloadpath+clean_filename(filename), 'wb') as f:
        f.write(videofile.content)
    print("download finished")


if __name__ == "__main__":
    links = get_streamable_videos_link(username,password)
    for url,filename,tag in links:
        download_vid(url,filename)
