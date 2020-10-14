from django import forms
import json
import requests

class KaKaoTalkForm(forms.Form):
    text = forms.CharField(label='전송할 Talk', max_length=300)
    web_url = forms.CharField(label='Web URL', max_length=300,
                        initial='http://192.168.0.21:8000/mjpeg?mode=stream')
    mobile_web_url = forms.CharField(label='Mobile Url', max_length=300,
                        initial='http://192.168.0.21:8000/mjpeg?mode=stream')

    def send_talk(self):
        talk_url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
        with open("access_token.txt", "r") as f:
            token = f.read()

        header = {"Authorization": f"Bearer {token}"}
        # text_template = {
        #     'object_type': 'text',
        #     'text': self.cleaned_data['text'],
        #     'link': {
        #         'web_url': self.cleaned_data['web_url'],
        #         'mobile_web_url': self.cleaned_data['mobile_web_url']
        #     },
        #     'button_title' : '카메라 보기'
        # }
        text_template = {
            "object_type": "location",
            "address" : "경기도 부천시 조마루로 135",
            "content": {
                "title": "달 사진",
                "description": "위치보기는 집으로",
                "image_url": "https://www.thisiscolossal.com/wp-content/uploads/2019/02/moon_crop-640x640.jpg",
                "image_width": 640,
                "image_height": 640,
                "link": {
                    "web_url": "http://www.daum.net",
                    "mobile_web_url": "http://m.daum.net",
                    "android_execution_params": "contentId=100",
                    "ios_execution_params": "contentId=100"
                }
            },
        }
        template_object={
            "object_type": "feed",
            "content": {
                "title": "ㅇㅇ",
                "image_url": "https://taegon.kim/wp-content/uploads/2018/05/image-5.png",
                "image_width": 640,
                "image_height": 640,
                "link": {
                    "web_url": "https://taegon.kim/wp-content/uploads/2018/05/image-5.png",
                    "mobile_web_url": "http://m.daum.net",
                    "android_execution_params": "contentId=100",
                    "ios_execution_params": "contentId=100"
                }
            },
            "social": {
                "like_count": 100,
                "comment_count": 200,
                "shared_count": 300,
                "view_count": 400,
                "subscriber_count": 500
            },
            "buttons": [
                {
                    "title": "웹으로 이동",
                    "link": {
                        "web_url": "http://www.daum.net",
                        "mobile_web_url": "http://m.daum.net"
                    }
                },
                {
                    "title": "위치보기",
                    "link": {
                        "address" : "경기도 부천시"
                    }
                }
            ]
        }

        print(text_template)
        payload = {'template_object': json.dumps(text_template)}
        res = requests.post(talk_url, data=payload, headers=header)

        return res, self.cleaned_data['text']