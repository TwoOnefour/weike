import os.path

import requests



def cancel_bind(session, userid):
    session.post("https://weiban.mycourse.cn/pharos/my/cancelBindWechat.do?timestamp={}".format(int(time.time())), verify=False, data={
        "userId": userid,
        "tenantCode": 43000010,
        "limit": 3
    })

if __name__ == "__main__":
    if os.path.exists("./token.txt", "r"):
        with open("./token.txt") as f:
            userid = f.readlines()[0]
    cancel_bind(requests.Session(), userid)