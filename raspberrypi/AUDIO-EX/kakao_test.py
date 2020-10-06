from kakao_dictation import *
from pyaudio_record import *
import io

audio_data = record(5) # 녹음 데이터 리스트

audio_stream = io.BytesIO() # 메모리의 있는 파일
save_wav(audio_stream, audio_data)

result = dictation(audio_stream.getvalue()) # wav 파일 내용 전달
print("인식결과", result)