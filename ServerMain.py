import ImageProcessing
import emailer
import cv2
import socket
import numpy
from server import Server


def process_image(data):
    image = numpy.load(data)
    cv2.imshow("test", image)
    cv2.waitKey(0)
    faces = ImageProcessing.detect_faces(image)
    print("Processed image.")
    if len(faces) > 0:
        print("Sending email.")
        _, encoded_img = cv2.imencode(".png", image)
        emailer.sendMail(["brian.semrau@gmail.com"], "Test Server Msg", "This is the content", [encoded_img])


if __name__ == '__main__':
    server = Server()
    ip = "169.254.207.37"  # socket.gethostbyname(socket.gethostname())
    port = 42069
    server.listen(ip, port)
    print("Server listening on {}:{}".format(ip, port))
    server.retrieve_data(process_image)
