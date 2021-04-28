import requests
import os

def song_download(song_id,name):
    url = 'http://link.hhtjim.com/163/{}.mp3'.format(song_id)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182'
                      ' Safari/537.36'
    }

    resp = requests.get(url=url, headers=headers)
    try:
        path_1 = 'F:\\wangyiyun\\download'
        if os.path.exists(path_1):
            pass
        else:
            os.mkdir(path_1)
        path_2 = path_1+'\\'+name.replace('/', '')
        if os.path.exists(path_2):
            pass
        else:
            os.mkdir(path_2)
        filename = name.replace('/', '').replace('_','') + '.m4a'

        with open(path_2+'\\'+filename, 'wb') as f:
            f.write(resp.content)
    except OSError:
        pass


# song_download('1839243729','_5:15 郭顶')