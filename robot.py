# -*- coding=utf-8 -*-
import requests
import itchat

KEY = '04f44290d4cf462aae8ac563ea7aac16'

def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
	print(msg)
    reply = get_response(msg['Text'])+'——你的小可爱'
    return reply

itchat.auto_login(enableCmdQR=True)
itchat.run()
