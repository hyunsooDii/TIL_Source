import cv2

class USBCam:
    def __init__(self, show = False, framerate = 25, width = 640,height= 480):
        self.size = (width,height)
        self.show = show
        self.framerate = framerate

        self.cap = cv2.VideoCapture(0) # 0번 카메라
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH,self.size[0])
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.size[1])

    def snapshot(self): # jpeg 이미지 1장 리턴
        retval, frame = self.cap.read() # 프레임 캡쳐, frame: numpy배열 - BGR
        if retval :
            _, jpg = cv2.imencode('.JPEG', frame) # _, True False를 받아주는 변수
            return jpg.tobytes()

class MJpegStreamCam(USBCam):
    def __init__(self, show = False, framerate = 25, width = 640,height= 480):
        super().__init__(show=show, framerate=framerate, width=width, height=height)

    def __iter__(self): # 열거 가능객체이기 위한 조건 for x in MJpegStreamCam() :
        while True:
            retval, frame = self.cap.read()
            _, jpg = cv2.imencode('.JPEG',frame)
            yield(
                b'--myboundary\n'
                b'Content-Type:image/jpeg\n'
                b'Content-Length: ' + f"{len(jpg)}".encode()+b'\n'
                b'\n' + jpg.tobytes() + b'\n'
            )