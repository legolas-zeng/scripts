# -*- coding: utf-8 -*-
import itchat, time
from itchat.content import TEXT
import io
#name = ' '
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
roomslist = []

itchat.auto_login(enableCmdQR = False)

def getroom_message(n):
    #获取群的username，对群成员进行分析需要用到
    itchat.dump_login_status() # 显示所有的群聊信息，默认是返回保存到通讯录中的群聊
    RoomList =  itchat.search_chatrooms(name=n)
    if RoomList is None:
        print("%s group is not found!" % (name))
    else:
        return RoomList[0]['UserName']

def getchatrooms():
    #获取群聊列表
    roomslist = itchat.get_chatrooms()
    print(roomslist)
    return roomslist

for i in getchatrooms():
    print(i['NickName'])
    roomslist.append(i['NickName'])

with io.open('C:\Users\Administrator\Desktop\huangsi.txt', 'w', encoding='utf-8')as f:
    for n in roomslist:
        ChatRoom = itchat.update_chatroom(getroom_message(n), detailedMember=True)
        for i in ChatRoom['MemberList']:
            #print (i['Province']+":",i['NickName'])
            f.write(i['Province']+":"+i['NickName']+'\n')
            print('正在写入           '+i['Province']+":",i['NickName'])
    f.close()

# for i in ChatRoom:
#     print(i['MemberList']['ContactList'])
#     count += 1
# print(count)

# # @itchat.msg_register(TEXT)
# # def simple_reply(TEXT):
# #     print(msg.text)
# #
# # itchat.auto_login(enableCmdQR = False,hotReload = True)  # enableCmdQR=True这一参数为二维码在下面控制台中显示出来，而不是用图片显示
# # itchat.run()
# itchat.auto_login(enableCmdQR = False)
#
# # time.sleep()
# # itchat.logout()
# # friends = itchat.get_friends()
# # for i in friends:
# #     print(i)
# rooms = itchat.get_chatrooms()
# for i in rooms:
#     print(i['NickName'])
#     memberList = itchat.update_chatroom(i['NickName'])
#     print (memberList)
#
# #     room = itchat.update_chatroom(i['NickName'],detailedMember = True)
# #     print(room)
# #     # for i in room:
# #     #     print(i)