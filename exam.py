import os
import time
import json
import openai
def send_to_chatGPT(question):
    openai.api_key = ""  # 填入chatGPT的api key

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": 'system', "content": "你是一个答题人"},
            {"role": 'user', "content": "请解析问题，根据选项内容作答，我将给出选项id和选项内容，只需要你返回正确选项的选项id"
                                        },
            {"role":"assistant", "content":"好的，我将只回复正确答案的选项id"},
            {"role": 'user', "content": "单选题, 问题：1+1等于几\n选项id：'ff65234', 选项内容:'2'\n选项id：'f34', 选项内容:'1'\n"},
            {"role": "assistant", "content": "ff65234"},
            {"role": 'user', "content": "多选题, 问题：以下哪个选项描述正确\n选项id：'ff6', 选项内容:'天是蓝色的'\n选项id：'f3', 选项内容:'草是绿色的'\n选项id：'f1', 选项内容:'草是白色的'\n"},
            {"role": "assistant", "content": "ff6,f3"},
            {"role": 'user',
             "content": "{}".format(question)},
        ]
    )
    time.sleep(5)
    return completion.choices[0].message["content"]


def exam(session,userid,userExamPlanId):
    return json.loads(session.post("https://weiban.mycourse.cn/pharos/exam/startPaper.do?timestamp={}".format(int(time.time()) + 1),data={
        "userExamPlanId":userExamPlanId,
        "tenantCode": 43000010,
        "userId":userid
    }, verify=False).text)

