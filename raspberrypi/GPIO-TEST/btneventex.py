import RPi.GPIO as GPIO
import time

# callable class
class BtnEventEx:
    def __init__(self):
        # 사용할 GPIO핀의 번호를 선정합니다.
        self.button_pin = 23
        self.led_pin = 18
        # 버튼 핀의 INPUT설정 , PULL DOWN 설정
        GPIO.setup(self.button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        # LED 핀의 OUT설정
        GPIO.setup(self.led_pin, GPIO.OUT)
        # boolean 변수 설정
        self.light_on = False

    def button_callback(self, channel):
        if self.light_on == False: # LED 불이 꺼져있을때
            GPIO.output(self.led_pin,1) # LED ON
            print("LED ON!")
        else: # LED 불이 져있을때
            GPIO.output(self.led_pin,0) # LED OFF
            print("LED OFF!")
        self.light_on = not self.light_on # False <=> True

    def __call__(self):
        self.light_on = False
        GPIO.add_event_detect(self.button_pin,GPIO.RISING, callback=self.button_callback, bouncetime=10)

        try:
            while 1:
                time.sleep(0.1) # 0.1초 딜레이
        except KeyboardInterrupt:
            GPIO.remove_event_detect(self.button_pin)