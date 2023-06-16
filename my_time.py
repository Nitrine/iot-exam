import time
from datetime import datetime
import requests
import my_sms
    
while(True):
    current_time = datetime.now()
    week_day = datetime.today().weekday()
    print(current_time.strftime('%H:%M:%S'))
    if week_day != 6:
        if current_time.strftime('%H:%M') == "18:00":
            print("SMS를 전송했습니다.")
            url = "http://api.coolsms.co.kr/messages/v4/send"
            headers = my_sms.get_headers("API KEY","API SECRET")
            data = '{"message":{"to":"수신자 전화번호","from":"발신자 전화번호","text":"Light on"}}'

            response = requests.post(url, headers=headers, data=data)
            print(response.status_code)
            print(response.text)
    time.sleep(60)

        
    

