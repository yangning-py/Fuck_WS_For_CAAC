import time
import json
import requests
import random
import datetime

# secrets字段录入
DEPTID = eval(input()) #专业代码
DEPTTEXT = input() #学院-专业-班级
STREET = input() #打卡位置所在道路
DISTRICT = input() #打卡位置所在区县
CITY = input() #打卡位置所在市
PROVINCE = input() #打卡位置所在省份
POIS = input() #打卡位置所在小区
LNG = input() #纬度
LAT = input() #经度
ADDRESS = input() #定位: 区县道路小区名
ADDRTEXT = input() #当前位置: 省份-城市
CUSTOMERID = input() #用途不明
STUNO = input() #学号/工号
USERNAME = input() #姓名
PHONENUM = input() #电话
USERID = input() #完美校园账号
AGE = input() #年龄
BASEPROVINCE = input() #家乡省份
BASECITY = input() #家乡城市
BASEAREA = input() #家乡区县
BASEADDR = input() #家乡详细地址
SCHOOLPOIS = input() #学生所在校区
WORK = input() #是否实习
TOKEN = input() #token,暂时不支持自动获取

# 小时数据修正 
now = time.localtime().tm_hour + 8
if (now >= 24):
    nowfix = now - 24
elif (now >= 0 ) & (now < 24):
    nowfix = now
else:
    print("fail,经过修正，现在的时间是%d点%d分" %(nowfix,time.localtime().tm_min))
    exit(0)

print("pass,经过修正，现在的时间是%d点%d分" %(nowfix,time.localtime().tm_min))
print("---------------")

# 时间戳
time.time()
print(time.time)
posttime = time.time()
print("pass,当前时间时间戳为%d" %(posttime))
print("---------------")


# 随机体温(36.3~36.8)
a = random.uniform(35.8, 36.8)
temperature = round(a,1)
print("pass,本次打卡使用体温为：%d" %(temperature))
print("---------------")

# 全局设置
sign_url = "https://reportedh5.17wanxiao.com/sass/api/epmpics"

headers = {
    'User-Agent': 'Chrome/87.0.4280.101 Mobile Wanxiao/5.1.5',
	'Content-Type': 'application/json',
	'Accept-Encoding': 'gzip, deflate'
}

# json体
jsons = {
    "businessType":"epmpics",
    "method":"submitUpInfo",
    "jsonData":
    {
        "deptStr":
        {
            "deptid": DEPTID,
            "text": DEPTTEXT
        },
        "areaStr":
        {
            "street": STREET,
            "district": DISTRICT,
            "city": CITY,
            "province": PROVINCE,
            "pois": POIS,
            "lng": LNG,
            "lat": LAT,
            "address": ADDRESS,
            "text": ADDRTEXT
        },
        "reportdate": posttime,
        "customerid": CUSTOMERID,
        "deptid": DEPTID,
        "source":"app",
        "templateid":"pneumonia",
        "stuNo": STUNO,
        "username": USERNAME,
        "phonenum": PHONENUM,
        "userid": USERID,
        "updatainfo":[ 
        {
            "propertyname":"age",
            "value": AGE
        },
        {
            "propertyname":"name",
            "value": USERNAME
        },
        {
            "propertyname":"jtdz",
            "value": BASEPROVINCE
        },
        {
            "propertyname":"levorgodata",
            "value": BASECITY
        },
        {
            "propertyname":"备注",
            "value": BASEAREA
        },
        {
            "propertyname":"返回及到达时间",
            "value": BASEADDR
        },
        {
            "propertyname":"ownPhone",
            "value": PHONENUM
        },
        {
            "propertyname":"jtcy",
            "value": "否"
        },
        {
            "propertyname":"medicalObservation",
            "value": SCHOOLPOIS
        },
        {
            "propertyname":"isGoWarningAdress",
            "value": "B.否"
        },
        {
            "propertyname":"isTouch",
            "value": "B.否"
        },
        {
            "propertyname":"ishborwh",
            "value": "B.否"
        },
        {
            "propertyname":"isis",
            "value":"B.否"
        },
        {
            "propertyname":"isleaveaddress",
            "value":"B.否"
        },
        {
            "propertyname":"tjjw0511",
            "value":"否"
        },
        {
            "propertyname":"medicalObservation1",
            "value":"B.否"
        },
        {
            "propertyname":"ownbodyzk",
            "value": WORK
        },
        {
            "propertyname":"isConfirmed",
            "value":"A.从未有过居家观察"
        },
        {
            "propertyname":"cxjh",
            "value":"A.从未有过集中观察"
        },
        {
            "propertyname":"fhhb",
            "value":"健康"
        },
        {
            "propertyname":"symptom",
            "value":"A.无症状"
        },
        {
            "propertyname":"sex",
            "value":"B.否"
        },
        {
            "propertyname":"xinqing",
            "value":"B.否"
        },
        {
            "propertyname":"isAlreadyInSchool",
            "value":"B.否"
        }
        ],
        "gpsType":1,
        "token": TOKEN
        }
    }

# POST打卡数据
response = requests.post(sign_url, json=jsons, headers=headers)
utcTime = (datetime.datetime.utcnow() + datetime.timedelta(hours=8))
cstTime = utcTime.strftime("%H时%M分%S秒")
print("---------------")
print(response.request.headers)
#print("---------------") #调试临时开启
#print(response.request.body) #调试临时开启
print("---------------")
print(response.text)
#print("---------------")

# 阶段1打卡情况判断
if response.json()["msg"] == '成功':
    msg = cstTime + "打卡成功"
else:
    msg = cstTime + "打卡异常"
print(msg)