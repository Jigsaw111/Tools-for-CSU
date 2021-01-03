import base64
from bs4 import BeautifulSoup
import requests
import re
import json
import config

res = requests.get(
    url="http://csujwc.its.csu.edu.cn/"
)
myCookie = res.cookies

nameBytes = base64.b64encode(bytes(config.username, encoding='utf-8'))
pwd = base64.b64encode(bytes(config.password, encoding='utf-8'))
datas = {
    'encoded' : nameBytes + b'%%%' + pwd
    # 账号密码的base64加密结果
}


res = requests.post(
    url="http://csujwc.its.csu.edu.cn/jsxsd/xk/LoginToXk",
    cookies=myCookie,
    data=datas
)
myCookie = res.cookies
data = {'type': 'xs0101', 'xnxq01id': config.semester,'xs0101id': config.id,'xs': config.name}
url = 'http://csujwc.its.csu.edu.cn/jiaowu/pkgl/llsykb/llsykb_kb.jsp'

req = requests.post(url, cookies=myCookie,data=data)

class_info={}

soup = BeautifulSoup(req.text, 'html.parser')
for week_day in range(1, 8):
    for class_time in range(1, 7):
        query_selector = 'div[id="' + re.findall(r"value=\"(.*)-7-1\">",req.text)[class_time-1] + '-' + str(week_day) + '-2"] a'
        for i in soup.select(query_selector):  # i 为 a 元素
            if(not str(week_day) in class_info):class_info[str(week_day)]={}
            class_info[str(week_day)][str(class_time)] = {
                            'clsname': i.contents[0],
                            'teacher': 'None' if not i.select('font[title="老师"]') else \
                                i.select('font[title="老师"]')[0].string,
                            'duration': 'None' if not i.select('font[title="周次"]') else \
                                i.select('font[title="周次"]')[0].string,
                            'week': 'None' if not i.select('font[title="单双周"]') else \
                                i.select('font[title="单双周"]')[0].string,
                            'location': 'None' if not i.select('font[title="上课地点教室"]') else \
                                i.select('font[title="上课地点教室"]')[0].string}
                                
with open("class_info.json",'w') as f:
    f.write(json.dumps(class_info,indent=4, ensure_ascii=False,separators=(',', ': ')))
