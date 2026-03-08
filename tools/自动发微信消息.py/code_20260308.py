import requests

def send_wechat(msg):
    # 企业微信机器人（你可以换成自己的）
    url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=demo"
    data = {
        "msgtype": "text",
        "text": {"content": msg}
    }
    requests.post(url, json=data)

send_wechat("自动化消息发送成功！")
print("✅ 消息发送成功！")
