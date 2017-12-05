from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
from client import ClientProtocol

if __name__ == '__main__':
    cam = PiCamera()
    cam.resolution = (240, 360)
    cam.framerate = 32
    raw_capture = PiRGBArray(cam, size=(240, 368))

    client = ClientProtocol()
    client.connect("169.254.207.37", 42069)  # TODO find server IP

    time.sleep(0.1)

    for frame in cam.capture_continuous(raw_capture, format='bgr', use_video_port=True):
        image = frame.array
        # scaled = cv2.resize(image, (240, int(240. * image.shape[0] / image.shape[1])))
        # send image over TCP
        client.send_image(image)

        time.sleep(10)
        raw_capture.truncate(0)
