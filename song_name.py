
import requests
import re

def song_name(song_id):
    url = 'https://music.163.com/song?id={}'.format(song_id)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182'
                      ' Safari/537.36'
    }
    resp = requests.get(url=url, headers=headers)
    name = re.compile(r'<title>(.*?)</title>').findall(resp.content.decode())[0]
    return (''.join(name.split(' -')[:2]))

# sac = song_name('254574')
# print(sac)
