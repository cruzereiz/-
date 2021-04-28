import random
import math
import base64
import codecs
from Crypto.Cipher import AES


#网易云音乐加密函数a，生成一个16位的随机字符串
def fun_a():
    orig = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    i = 0
    str = ''
    while i < 16:
        e = random.random() * len(orig)
        e = math.floor(e)
        str += list(orig)[e]
        i += 1
    return str

#网易云音乐加密函数b，对参数1和参数4进行AES加密，其中参数1为加密内容，参数4为密钥
def fun_b(msg,key):
    padding = 16 - len(msg) % 16
    msg = msg + padding * chr(padding)
    msg = msg.encode('utf-8')
    key = key.encode('utf-8')
    iv = '0102030405060708'.encode('utf-8')
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encryptedbytes = cipher.encrypt(msg)
    encodestrs = base64.b64encode(encryptedbytes)
    enctext = encodestrs.decode('utf-8')
    return enctext

#网易云音乐加密函数c，对参数2、参数3和func_a函数生成的16位随机字符串进行RSA加密
def fun_c(strs):
    key = '010001'
    f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341' \
        'f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e8204' \
        '7b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
    string = strs[::-1]
    text = string.encode('utf-8')
    seckey = int(codecs.encode(text, encoding='hex'), 16)**int(key, 16) % int(f, 16)
    return format(seckey, 'x').zfill(256)

#网易云音乐加密函数d，生成encText和encSeckey参数，其中enctext是param，encseckey是encSeckey。msg的数据样式如下面demo
def fun_d(msg):
    a = fun_a()
    aes_k1 = '0CoJUm6Qyw8W8jud'
    aes_res1 = fun_b(msg,aes_k1)
    enctext = fun_b(aes_res1,a)
    encseckey = fun_c(a)
    return enctext,encseckey



# msg = '{"rid":"R_SO_4_1492901593","threadId":"R_SO_4_1492901593","pageNo":"1","pageSize":"20","cursor":"-1","
# offset":"0","orderType":"1","csrf_token":""}'
# asd = fun_d(msg)
# print(asd[0])
# print('\n')
# print(asd[1])
