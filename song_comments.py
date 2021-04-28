
import requests
import json
import os


def hotcomments_get(encs,name):
    url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182'
                      ' Safari/537.36'
    }

    data = {
        'params': encs[0],
        'encSecKey': encs[1]}
    #网易云音乐热评爬取，共15条评论，包含用户昵称，用户id，评论内容及点赞数
    resp = requests.post(url=url, headers=headers, data=data)
    hotcom_list = json.loads(resp.content.decode())['data']['hotComments']
    print(len(hotcom_list))
    for com in hotcom_list:
        item = {}
        item['name'] = com['user']['nickname']
        item['id'] = com['commentId']
        item['content'] = com['content']
        item['count'] = com['likedCount']
        print(item)
        print('\n')

        try:
            path_1 = 'F:\\wangyiyun\\download'
            if os.path.exists(path_1):
                pass
            else:
                os.mkdir(path_1)
            path_2 = path_1 + '\\' + name.replace('/', '')
            if os.path.exists(path_2):
                pass
            else:
                os.mkdir(path_2)
            filename = name.replace('/', '').replace('_', '') + '.txt'

            # with open(path_2 + '\\' + filename, 'wb') as f:
            #     f.write(resp.content)
            with open(path_2 + '\\' + filename, 'a+', encoding='utf-8') as f:
                f.write(json.dumps(item, ensure_ascii=False, ))
        except OSError:
            pass


