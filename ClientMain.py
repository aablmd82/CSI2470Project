from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

cam = PiCamera()
raw_capture = PiRGBArray(cam)

time.sleep(0.1)

while True:
    cam.capture(raw_capture, format='bgr')
    image = raw_capture.array
    scaled = cv2.resize(image, (240, int(240. * image.shape[0] / image.shape[1])))
    # send image over TCP
    cv2.imshow("test", scaled)
    cv2.waitKey(0)
