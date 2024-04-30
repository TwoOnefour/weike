# 描述
这是微信公众号安全微伴\微课的自动刷课程序，可以完成课程视频，使用gpt的api_key可以自动答题

# 用法
`pip install -r requirements.txt`安装依赖

`python main.py`

输入你的学号即可自动刷课

# 答题（可选）

不推荐使用，因为自己答题更容易拿80分及格，使用gpt-4很贵，去年测试使用gpt-3.5一般只有50-60分，而且浪费考试次数

如果需要使用gpt,请在exam.py中添加

`openai.proxy = "http://127.0.0.1:10808"`

其中127.0.0.1:10808为你的代理ip和端口

并取消main.py中最后几行finish_exam()的注释


# Description and Configuration
This is a weike script automatically finishing the course and exam in weike.
# Configuration
## Module

It bases on requests

```pip install requests```
or
```pip install -r requirements.txt```

## Modify the Config
Use your own Student ID then run the code.

Please note that the progress won't be make if the sleep time being set too low.

You can modify Student ID in line 11 and sleep time in line 16.

## Cancel Binding
![image](https://user-images.githubusercontent.com/77989499/230581033-da1cee09-6691-434f-ac0a-e41de75bb9ad.png)

# Usage

```python ./main.py```

if the program is interrupted by any reason, please run ```python ./cancel_bind.py``` to make sure the account not be associate with any openid.

Make issue if any question exists.

![image](https://user-images.githubusercontent.com/77989499/230560632-97563819-e665-477b-a940-6088981b9e02.png)

# About GPT
exam() function uses GPT's API to solve the exam problem. It may not get high score while it is convenient.
