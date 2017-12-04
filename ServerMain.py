import ImageProcessing
import emailer
import cv2
# TODO import tcpserver


def process_image(image):
    faces = ImageProcessing.detect_faces(image)
    if len(faces) > 0:
        _, encoded_img = cv2.imencode(".png", image, )
        emailer.sendMail(["brian.semrau@gmail.com"], "Test Server Msg", "This is the content", [encoded_img])


if __name__ == '__main__':
    while True:
        # Wait to receive TCP data
        pass
