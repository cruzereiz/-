
import requests
import time

from song_list import list_id
from song_name import song_name
from song_down import song_download
from canshu_a import canshu_a
from crypto_func import fun_d
from song_comments import hotcomments_get


playlist = '5453912201'
#获取歌单列表中的歌曲id
song_ids = list_id(playlist)
for song_id in song_ids:
    print(song_id)
    # 通过歌曲id，获取歌曲名和作者
    name = song_name(song_id)
    # 通过歌曲id，下载歌曲
    song_download(song_id,name)
    # print(name + '下载完成。')

    #根据歌曲id，构造破解参数a。
    cans_a = canshu_a(song_id)

    # 根据歌曲id，构造破解参数encText和encSeckey。
    encs = fun_d(cans_a)

    # 根据歌曲构造破解参数encText和encSeckey，下载歌曲热门评论共15条。
    hotcomments_get(encs,name)












