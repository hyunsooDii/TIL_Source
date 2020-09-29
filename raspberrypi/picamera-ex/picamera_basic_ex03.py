import picamera
from time import sleep
with picamera.Picamera() as camera:
    camera.start_preview()

    for i in range(5):
        sleep(5)
        camera.capture(f'/home/pi/image{i}.jpg')

    camera.stop_preview()