import requests
import re

def list_id(id):
    # url = 'http://music.163.com/discover/toplist'
    url = 'http://music.163.com/discover/toplist?id={}'.format(id)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
    }
    resp = requests.get(url=url, headers=headers)
    html = resp.content.decode()
    text = re.compile(r'<textarea id="song-list-pre-data" style="display:none;">(.*?)</textarea>')
    res = text.findall(html)[0]
    #正则匹配歌曲id，已完成。
    song_id = re.compile(r'"commentThreadId":"R_SO_4_(.*?)"')
    ids = song_id.findall(res)
    return ids



#
# sds = list_id('3778678')
# print(sds)
