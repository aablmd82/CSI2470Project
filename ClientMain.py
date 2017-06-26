from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

cam = PiCamera()
cam.resolution = (240, 360)
cam.framerate = 32
raw_capture = PiRGBArray(cam, size=(240, 360))

time.sleep(0.1)

for frame in cam.capture_continuous(raw_capture, format='bgr', use_video_port=True):
    image = frame.array
    # scaled = cv2.resize(image, (240, int(240. * image.shape[0] / image.shape[1])))
    # send image over TCP
    print("send image TODO")
    # cv2.imshow("test", image)
    # cv2.waitKey()
    raw_capture.truncate(0)

