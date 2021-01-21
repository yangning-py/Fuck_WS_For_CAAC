import json
import requests

# secrets字段录入
CUSTOMERID = input() #用途不明

# 全局设置
sign_url = "https://reportedh5.17wanxiao.com/api/remind/openRemind"

headers = {
    'User-Agent': 'Chrome/87.0.4280.101 Mobile Wanxiao/5.1.5',
	'Content-Type': 'application/json',
	'Accept-Encoding': 'gzip, deflate'
}

#json体2
jsons = {
    customerId=CUSTOMERID
}

# POST打卡数据
response = requests.post(sign_url, json=jsons, headers=headers)
utcTime = (datetime.datetime.utcnow() + datetime.timedelta(hours=8))
cstTime = utcTime.strftime("%H时%M分%S秒")
print("---------------")
print(response.request.headers)
print("---------------") #调试临时开启
print(response.request.body) #调试临时开启
print("---------------")
print(response.text)
#print("---------------")

# 打卡情况判断
if response.json()["msg"] == 'success':
    msg = cstTime + "打卡成功"
else:
    msg = cstTime + "打卡异常"
print(msg)