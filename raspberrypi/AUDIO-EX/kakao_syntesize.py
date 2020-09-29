import requests
import io
from pydub import AudioSegment
from pydub.playback import play

URL = "https://kakaoi-newtone-openapi.kakao.com/v1/synthesize"
HEADERS = {
    "Content-Type" : "application/xml",
    "Authorization" : "KakaoAK de5f167d646efcbf8021b575867fe002"
}

DATA = """
<speak>
    그는 그렇게 말했습니다.
    <voice name="MAN_DIALOG_BRIGHT">잘 지냈어? 나도 잘 지냈어.</voice>
    <voice name="WOMAN_DIALOG_BRIGH" speechStyle="SS_ALT_FAST_1">금요일이 좋아
    요.</voice>
</speak>
"""
res = requests.post(URL, headers = HEADERS, data = DATA.encode('utf-8'))
# 음성 합성 결과를 파일로 저장하기
with open("result.mp3", "wb") as f:
    f.write(res.content)

sound = io.BytesIO(res.content)
song = AudioSegment.from_mp3(sound)

song = AudioSegment.from_mp3("./result.mp3")
play(song)