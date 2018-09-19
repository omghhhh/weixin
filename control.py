import itchat
import cv2
import time
import os


flag = 0   #消息开关助手
sendMsg = u"{消息助手}：暂时无法回复"
usageMsg = u'使用方法：\n1.运行CMD命令:cmd xxx\n'\
    u"-例如关机命令：\ncmd shutdown -s -t 0 \n"\
    u"2.获取当前电脑用户：cap\n3.启用消息助手（默认关闭）：ast\n"\
    u"4.关闭消息助手：astc"
nowtime = time.localtime()
filename = str(nowtime.tm_mday)+str(nowtime.tm_hour)+str(nowtime.tm_min)+str(nowtime.tm_sec)+".txt"
myfile = open(filename,'w')


@itchat.msg_register('TEXT')
def text_reply(msg):
    global flag
    message = msg['Text']
    fromName = msg['FromUserName']
    toName = msg['ToUserName']

    if toName=="filehelper":
        if message == 'cap':
            cap = cv2.VideoCapture(0)
            time.sleep(300)
            print(cap.isOpened())
            ret,img = cap.read()
            cv2.imwrite("weixinTemp.jpg", img)
            itchat.send('@img@%s'%u'weixinTemp.jpg','filehelper')
            cap.release()
        if message[0:3] == 'cmd':
            os.system(message.strip(message[0:4]))
        if message == 'ast':
            flag = 1
            itchat.send('消息助手开启','filehelper')
        if message == 'astc':
            flag = 0
            itchat.send('消息助手关闭','filehelper')
    elif flag == 1:
        itchat.send(sendMsg,fromName)
        myfile.write(message)
        myfile.write('\n')
        myfile.flush()

if __name__ == '__main__':
    itchat.auto_login()
    itchat.send(usageMsg,"filehelper")
    itchat.run()


