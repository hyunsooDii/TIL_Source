from gpiozero import DistanceSensor
import io
import random
from picamera import PiCamera, PiCameraCircularIO

sensor = DistanceSensor(24, 23)

def motion_detected():
    print("detected")
    return sensor.distance <= 0.2
print("start")

camera = PiCamera()
stream = PiCameraCircularIO(camera, seconds=20)

camera.start_recording(stream, format='h264')
print("ready")
try:
    while True:
        print("while")
        # camera.wait_recording(1)
        if motion_detected():
            print('motion detected')
            camera.start_preview()
            camera.wait_recording(10)
            camera.stop_preview()
            stream.copy_to('motion.h264')
finally:
    camera.stop_recording()
