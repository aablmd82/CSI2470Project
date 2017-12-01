import cv2

cam = cv2.VideoCapture(0)

while True:
    ret, image = cam.read()
    scaled = cv2.resize(image, (240, int(240. * image.shape[0] / image.shape[1])))
    # send image over TCP
    cv2.imshow("Videocapture", scaled)
