#  修改完以后执行这个文件
import WeChat
import time
# 用while实现每天定时发送
# while(1):
#         currentHour = int(time.strftime("%H"))
#         print(currentHour)
#         if currentHour==8:  # 设置发送时间是每天8点
#             print("It's time")
#             openid = ''  #openid就是微信公众平台上的用户id，也就是你要给谁发
#             my_wechat=WeChat.WeChat(openid)
#             my_wechat.post_data()
#             print("success ,sleep........")
#             time.sleep(30)
#         if currentHour == 6:
#             print("itstimerightnow")
#             time.sleep(60)
#         else:
#             print("It's not time ,sleep........")
#             time.sleep(3600)


#下面三行代码可以进行测试，把while下的代码注释掉运行下面的代码，可以先发给自己测试效果
openid = 'oG2jL55tInMiTR9_mK6q6UFcOLks'  #openid就是微信公众平台上的用户id，也就是你要给谁发
my_wechat=WeChat.WeChat(openid)
my_wechat.post_data()

#openid = 'oG2jL5zT5YI23vvSwPFtHKHeykrA'  #openid就是微信公众平台上的用户id，也就是你要给谁发
#my_wechat=WeChat.WeChat(openid)
#my_wechat.post_data()


