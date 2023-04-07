import random

import requests
import time
import json
import urllib
import urllib3
urllib3.disable_warnings()
session = requests.Session()
userprojectid = "" # 填入自己的，下面略
userid = ""
username = ""
headers = {
    "Host": "weiban.mycourse.cn",
    "Accept": "*/*",
    "Connection": "keep-alive",
    "X-Token":"63501030-78bc-4811-b191-e56e52e5982a",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.34(0x1800222f) NetType/WIFI Language/en",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://weiban.mycourse.cn/index.html",
    "Accept-Encoding": "gzip, deflate, br"
}
session.headers.update(headers)
# session.cookies.update({
#     "Hm_lpvt_05399ccffcee10764eab39735c54698f":"1680840829",
#     "m_lvt_05399ccffcee10764eab39735c54698f":"1680828613,1680832674,1680833646,1680835279",
#     "SERVERID": "SERVERID=9ee29c682be9356b7648e0eed94165c1|1680841348|1680840817"
# })

def get_category_id(session):
    data = {
        "userProjectId": userprojectid,
        "chooseType":3,
        "userId": userid,
        "tenantCode": 43000010
    }
    result = session.post("https://weiban.mycourse.cn/pharos/usercourse/listCategory.do?timestamp={}".format(int(time.time())), data=data,verify=False)
    return json.loads(result.text)
def get_course_id(session):
    while True:
        result = get_category_id(session)
        for i in result["data"]:
            data = {
                "userProjectId": userprojectid, # 自己的userprojectid
                "chooseType": 3,
                "userId": userid, # 自己的userid
                "tenantCode": 43000010,
                "categoryCode": i["categoryCode"]
            }
            result1 = session.post(
                "https://weiban.mycourse.cn/pharos/usercourse/listCourse.do?timestamp={}".format(int(time.time())),
                data=data,verify=False).text
            result1 = json.loads(result1)
            for j in result1["data"]:
                if j["finished"] == 1:
                    continue
                data = {
                    "courseId": j["resourceId"],
                    "userProjectId": userprojectid,
                    "tenantCode": 43000010,
                    "userId": userid,
                }
                result2 = session.post(
                    "https://weiban.mycourse.cn/pharos/usercourse/getCourseUrl.do?timestamp={}".format(int(time.time())),
                    data=data,verify=False).text
                # print(result1.text)
                result3 = session.post(
                    "https://weiban.mycourse.cn/pharos/usercourse/study.do?timestamp={}".format(int(time.time())),
                    data=data, verify=False)
                url = json.loads(result2)["data"]
                parseResult = urllib.parse.urlparse(url)
                token = parseResult.query.split("&")[3][12:]
                data["type"] = 1
                # data["methodToken"] = token
                data["csCom"] = False
                data["userName"] = username # 填入自己的username
                data["weiban"] = "weiban"
                data["link"] = j["praiseNum"]
                result4 = requests.get(url, verify=False,params=data,headers={
                "referer": "https://weiban.mycourse.cn/",
                "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.34(0x1800222f) NetType/WIFI Language/en",
                })
                time.sleep(60)  # 这里要等一下，不然刷不了
                finish_course(session, j["userCourseId"], parseResult.query.split("&")[3][12:])


def finish_course(session, userCourseId, token):
    # headers = {
    # "Host":" weiban.mycourse.cn",
    # "Accept":" */*",
    # "Connection":" keep-alive",
    # "Cookie":" SERVERID=9ee29c682be9356b7648e0eed94165c1|1680828686|1680828611; Hm_lpvt_05399ccffcee10764eab39735c54698f=1680828613; Hm_lvt_05399ccffcee10764eab39735c54698f=1680828613",
    # "User-Agent":" Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.34(0x1800222f) NetType/WIFI Language/en",
    # "Accept-Language":" en-US,en;q=0.9",
    # "Referer": "https//mcwk.mycourse.cn/",
    # "Accept-Encoding":" gzip, deflate, br"
    # }
    # courseIdArr = get_course_id()
    # session.get("https://weiban.mycourse.cn/pharos/usercourse/getCourseUrl.do")

    params = {
        "callback":"jQuery341{}_{}".format(str(random.random()).replace(".", ""), int(time.time() * 1000)),
        "userCourseId": userCourseId, # "559d968b-a289-4fa5-a89d-e48d68af85e"
        "tenantCode": "43000010",
        "_": int(time.time() * 1000)+1,
    } # expando: "jQuery" + (f + Math.random()).replace(/\D/g, ""),
    result = requests.get("https://weiban.mycourse.cn/pharos/usercourse/v1/{}.do?".format(token), params=params,headers={
    "Host": "weiban.mycourse.cn",
    "Accept": "*/*",
    "Connection": "keep-alive",
    # "X-Token":"63501030-78bc-4811-b191-e56e52e5982a",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.34(0x1800222f) NetType/WIFI Language/en",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Referer": "https://mcwk.mycourse.cn/",
    "Accept-Encoding": "gzip, deflate, br"
},cookies={"SERVERID":session.cookies.get("SERVERID")}, verify=False)
    # print(1)
    # print(result)
get_course_id(session)
