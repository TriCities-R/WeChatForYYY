import datetime
import requests
import json


class WeChat():
    def __init__(self, openid):
        self.openid = openid
        self.data = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def get_token(self):  # 获取token，每两个小时获取一次
        try:
            with open("access_token.txt", "r") as f:
                content = f.read()
                data_dict = eval(content)
                time = datetime.datetime.strptime(data_dict["time"], '%Y-%m-%d %H:%M:%S')

            if (datetime.datetime.now() - time).total_seconds() < 7000:
                print("未到两小时，从文件读取")
                return data_dict["access_token"]
            else:
                # 超过两小时，重新获取
                print("超过两小时，重新获取")
                payload = {
                    'grant_type': 'client_credential',
                    'appid': 'wx48a732e898d6c050',  # 公众号appid,按自己实际填写
                    'secret': '4afb37e85b28000562fbc062b0c223ff',  # 按自己实际填写  这两个都在微信公众平台上
                }
                url = "https://api.weixin.qq.com/cgi-bin/token?"

                try:
                    respone = requests.get(url, params=payload, timeout=50)
                    access_token = respone.json().get("access_token")
                    nowtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    content = ("{\"access_token\":\"%s\",\"time\":\"%s\"}" % (access_token, nowtime))
                    # 写入文件
                    with open("access_token.txt", "w") as f:
                        f.write(content)

                    print("get_token", access_token)
                    return access_token
                except Exception as e:
                    print(e)
        except Exception as e:
            print("get_token,file", e)

    # def post_data(self):
    #     today = datetime.datetime.now().strftime('%Y-%m-%d')  # 获取今天的时间
    #     week_list = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]  # 改成日期
    #     week = week_list[datetime.datetime.now().weekday()]
    #     date = today + week
    #     url = 'https://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city=邢台'
    #     response = requests.get(url).text
    #     weatherDict = json.loads(response)
    #     # 将天气信息赋值给变量
    #     weatherlist = weatherDict.get('data').get('list')[0]
    #     weather = weatherlist.get('weather')
    #     min_temperature = str(weatherlist.get('low')) + '℃'
    #     max_temperature = str(weatherlist.get('high')) + '℃'
    #     starttime = datetime.datetime.strptime('2016-03-25', '%Y-%m-%d')  # 这个是在一起的日子，记得改成自己的，按照给出的格式改
    #     nowtime = datetime.datetime.now()
    #     love_day = str(nowtime.__sub__(starttime))[0:4]
    #     url = 'http://open.iciba.com/dsapi/'
    #     res = requests.get(url)
    #     daytip = res.json()['content']  # 这个是每日一句英语，每天都不一样
    #     data = {
    #         "touser": self.openid,
    #         "template_id": "d2IWEv9jWracHgd7mzILrv0klGdHDwk0LVu0AJuz2uY",  # 模板ID
    #         "data": {
    #             "date": {
    #                 "value": date,
    #                 "color": "#FF69B4"
    #             },
    #             "city": {
    #                 "value": '邢台',
    #                 "color": "#173177"
    #             },
    #             "weather": {
    #                 "value": weather,
    #                 "color": "#FF6347"
    #             },
    #             "min_temperature": {
    #                 "value": min_temperature,
    #                 "color": "#00FA9A"
    #             },
    #             "max_temperature": {
    #                 "value": max_temperature,
    #                 "color": "#DC143C"
    #             },
    #             "love_day": {
    #                 "value": love_day,
    #                 "color": "#FFFFCC"
    #             },
    #             "daytip": {
    #                 "value": daytip,
    #                 "color": "#F5DEB3"
    #             },
    #
    #         }
    #     }
    def post_data(self):
        today = datetime.datetime.now().strftime('%Y-%m-%d')  # 获取今天的时间
        week_list = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]  # 改成日期
        week = week_list[datetime.datetime.now().weekday()]
        date = today + week
        url = 'https://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city=渝北'
        url_chp = 'http://api.tianapi.com/caihongpi/index?key=76603766909146e832ae9a4ffd949804'
        response = requests.get(url).text
        response_chp = requests.get(url_chp).text
        weatherDict = json.loads(response)
        chpDict = json.loads(response_chp)
        chplist = chpDict.get('newslist')[0]
        chp = chplist.get('content')
        # 将天气信息赋值给变量
        weatherlist = weatherDict.get('data').get('list')[0]
        weather = weatherlist.get('weather')
        airData = weatherlist.get('airData')
        airQuality = weatherlist.get('airQuality')

        min_temperature = str(weatherlist.get('low')) + '℃'
        max_temperature = str(weatherlist.get('high')) + '℃'
        starttime = datetime.datetime.strptime('2021-10-10', '%Y-%m-%d')  # 这个是在一起的日子，记得改成自己的，按照给出的格式改
        marrytime = datetime.datetime.strptime('2022-5-5', '%Y-%m-%d')  # 这个是在一起的日子，记得改成自己的，按照给出的格式改
        nowtime = datetime.datetime.now()
        love_day = str(nowtime.__sub__(starttime))[0:4]
        marry_day = str(nowtime.__sub__(marrytime))[0:4]
        url = 'http://open.iciba.com/dsapi/'
        res = requests.get(url)
        daytip = res.json()['content']  # 这个是每日一句英语，每天都不一样
        data = {
            "touser": self.openid,
            # "template_id":"VOFg_dg_sgheR9zbi78kkb0gt6IQIZNEgsTqbYK_zqs",# 天气1
            # "template_id": "F-aQ2XGAPajeZ6r4wjNctDFdDsTQQYdhI9ptSX269a4",  # 天气2
            "template_id": "d2IWEv9jWracHgd7mzILrv0klGdHDwk0LVu0AJuz2uY",  # 宝贝每日天气预报
            "data": {
                "date": {
                    "value": date,
                    "color": "#E85827"  # 爱马仕橙
                },
                "city": {
                    "value": '渝北',
                    "color": "#517693"  # 马耳他蓝
                },
                "weather": {
                    "value": weather,
                    # "color":"#FADA5E" # 拿坡里黄
                    # "color": "#470024"  # 勃艮第红
                    # "color": "#E85827"  # 爱马仕橙
                    "color": "#8481BA"  # 紫色

                },
                "min_temperature": {
                    "value": min_temperature,
                    # "color":"#8F4B28" # 木乃伊棕
                    # "color":"#492D22" # 范戴克棕
                    "color": "#002FA7"  # 克莱因蓝
                },
                "max_temperature": {
                    "value": max_temperature,
                    # "color": "#002FA7"  # 克莱因蓝
                    "color": "#B9181A"  # 红色
                },
                "love_day": {
                    "value": love_day,
                    "color": "#470024"  # 勃艮第红
                },
                "daytip": {
                    "value": daytip,
                    "color": "#003153"  # 普鲁士蓝
                },
                "airData": {
                    "value": airData,
                    "color": "#D44848"  # 提香红
                },
                "airQuality": {
                    "value": airQuality,
                    "color": "#81D8D0"  # 蒂芙尼蓝
                },
                "chp": {
                    "value": chp,
                    # "color": "#E85827" # 爱马仕橙
                    "color": "#01847F"  # 马尔斯绿
                },
                "marry_day": {
                    "value": marry_day,
                    # "color": "#E85827" # 爱马仕橙
                    "color": "#01847F"  # 马尔斯绿
                },
            }
        }
        json_template = json.dumps(data)
        access_token = self.get_token()
        print("access_token--", access_token)
        url = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=" + access_token
        try:
            respone = requests.post(url, data=json_template, timeout=50)
            # 拿到返回值
            errcode = respone.json().get("errcode")
            print("test--", respone.json())
            if (errcode == 0):
                print("模板消息发送成功")
            else:
                print("模板消息发送失败")
        except Exception as e:
            print("test++", e)
