import os.path
import time
import requests
import random

def login(session):
    global userid, username, userprojectid
    if os.path.exists("./token.txt"):
        with open("./token.txt", "r") as f:
            result = f.readlines()
            userid = result[0].strip("\n")
            username = result[1].strip("\n")
            userprojectid = result[2].strip("\n")
        return
    openid = ""
    for i in range(28):
        if (i + random.randint(65, 91)) % 2 == 0:
            openid += chr(random.randint(65, 90))
        else:
            openid += chr(random.randint(97, 122))
    result = session.post("https://weiban.mycourse.cn/pharos/login/bindWechat.do?timestamp={}".format(int(time.time())),verify=False,data={
        "sno": sno,
        "password": sno,
        "openid": openid,  # 这个可以为假，位数正确即可 "oeNCVuNUTOo9YSuBDVasVYCY0vsB"
        "tenantCode":43000010,
        "type":1
    })
    result = json.loads(result.text)
    try:
        if result["msg"] == "该用户已经绑定过微信！":
            print("请解绑微信和账号的关联，进入安全微伴-->我的-->解除微信绑定")
            return
    except Exception as e:
        pass
    userid = result["data"]["userId"]
    username = result["data"]["userName"]
    result = session.post("https://weiban.mycourse.cn/pharos/index/listStudyTask.do?timestamp={}".format(int(time.time())), verify=False, data={
        "userId": userid,
        "tenantCode": 43000010,
        "limit": 3
    })
    result = json.loads(result.text)
    userprojectid = result["data"][0]["userProjectId"]
    with open("./token.txt", "w") as f:
        f.write(userid + "\n")
        f.write(username + "\n")
        f.write(userprojectid)
def cancel_bind(session, userid):
    print(session.post("https://weiban.mycourse.cn/pharos/my/cancelBindWechat.do?timestamp={}".format(int(time.time())), verify=False, data={
        "userId": userid,
        "tenantCode": 43000010,
        "limit": 3
    },headers = {
    "Host": "weiban.mycourse.cn",
    "Accept": "*/*",
    "Connection": "keep-alive",
    # "X-Token":"63501030-78bc-4811-b191-e56e52e5982a",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.34(0x1800222f) NetType/WIFI Language/en",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://weiban.mycourse.cn/index.html",
    "Accept-Encoding": "gzip, deflate, br"
}))


if __name__ == "__main__":
    userid = ""
    username = ""
    userprojectid = ""
    session = requests.Session()
    if os.path.exists("./token.txt"):
        with open("./token.txt", "r") as f:
            result = f.readlines()
            userid = result[0]
            username = result[0]
            userprojectid = result[0]
    else:
        sno = "" # 你的学号
    login(session)
    cancel_bind(session, userid)